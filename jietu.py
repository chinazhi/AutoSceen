
from PIL import ImageGrab
from aip import AipOcr 
from ctypes import *
import pyautogui
import random
import time
import os
import hashlib

# 百度OCR APPID AK SK 
APP_ID = '23956565'
API_KEY = 'NvEtcxo3GlkYYT0doWsawKz7'
SECRET_KEY = 'ZYpY4fnBjhyX605ZPP6VOMCY38TeyTG6'
# 连接百度OCR
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 全局变量 截图序号 重复的次数 文字、图片MD5值 图片位置 目标文件 MD5文件  
n = 0
repetition_num = -1
result_md5_list = []
picture_md5_list = []
imagefilepath = "D:\\tupian\\original_picture\\"
targetflie = "D:\\tupian\\study.txt"
result_md5_file = "D:\\tupian\\result_md5.txt"
picture_md5_file = "D:\\tupian\\picture_md5.txt"

# 读取图片 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 固定位置截图
def get_screen_info(imagefilepath):
    global n
    n += 1
    im = ImageGrab.grab(bbox=(800, 365, 1120, 710))
    im.save(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')  

# 解析图片文字 并拼接保存文字
def get_pic_text(filePath):  
    # 调用百度通用文字识别, 图片参数为本地图片 
    image = get_file_content(filePath)
    info = client.basicGeneral(image)

    nums = info['words_result_num']
    words_res = info['words_result']
    result = ''
    st_flag = '党史小知识'
    start = 0

    for i in range(nums):
        tmp = words_res[i]['words']
        #开始标志 有开头或者 1、字符时表示开始
        if((start == 0)):
            if(tmp == st_flag):
                start = 1
                continue
            if((tmp.find("1、") >= 0)):
                start = 1

        #结束标志 
        if(tmp.isdigit()):
            break
        #拼接json字符
        if(start) :
            result += tmp

    return result

# 将结果保存至指定文件中
def save_result_to_file(fliename ,result):  
    result += '\n'
    txt_file = open(fliename, 'a+', encoding='utf-8')
    txt_file.write(result)
    txt_file.close()
    print(result) 

# 获取图片MD5数值
def get_file_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5= hashlib.md5(data).hexdigest()
    return file_md5

# 分析图片的MD5数值，用于过滤重复
def analyse_picture_md5(picture_path):
    global n
    global picture_md5_file
    global picture_md5_list
    pic_md5 = get_file_md5(picture_path + ('0000' + str(n))[-4:] + '.jpg')

    if(pic_md5 in picture_md5_list):
        print("图片重复，放弃保存，QAQ ！")
        return 0
    else:
        picture_md5_list.append(pic_md5)
        save_result_to_file(picture_md5_file , pic_md5)
        return 1  

# 分析返回结果的MD5值，用于过滤重复
def analyse_result_md5(result):
    global result_md5_file
    global result_md5_list

    res_md5 = hashlib.md5(bytes(result, encoding="utf8")).hexdigest()

    if(len(result) < 3):
        print("接收到的字符异常，直接退出！")
        return -1
    #判断是否有重复MD5值存在，存在则不写入不存在则写入
    if(res_md5 in result_md5_list):
        print("文本重复，放弃保存，QAQ ！")
        return 0
    else:
        result_md5_list.append(res_md5)
        save_result_to_file(result_md5_file , res_md5)
        return 1   

# 判断本次读取是否要写入文本
def judge_result(picture_path, result):
    global targetflie
    global repetition_num
    # 2次MD5均不同则写入
    if(analyse_picture_md5(picture_path) and analyse_result_md5(result) ):
        save_result_to_file(targetflie, result)
        repetition_num = 0
    else:
        repetition_num = repetition_num + 1 
        return 0

# 重新拉起小程序
def restart_applet():
    global repetition_num  
    if(repetition_num >10 or repetition_num == -1):
        repetition_num = 0
        # 回到我的界面
        pyautogui.click(1120, 850, clicks=1, interval=0.0, button='left')
        time.sleep(2)
        # 点击关闭
        pyautogui.click(1137, 177, clicks=1, interval=0.0, button='left')
        time.sleep(2)
        # 点击小程序入口
        pyautogui.click(640, 715, clicks=1, interval=0.0, button='left')
        time.sleep(2)
        # 点击小程序
        pyautogui.click(728, 328, clicks=1, interval=0.0, button='left')
        time.sleep(10)
        print("重启小程序")

#固定位置拉起小程序
restart_applet()

while 1:
    #随机点击菜单 《我的》
    randnum1 = random.randrange(0,15)
    randnum2 = random.randrange(0,10)
    pyautogui.click(1120 - randnum1, 850 + randnum2, clicks=1, interval=0.0, button='left')
    time.sleep(4)

    #随机点击菜单 《首页》
    randnum1 = random.randrange(0,15)
    randnum2 = random.randrange(0,10)
    pyautogui.click(800 + randnum1, 850 - randnum2, clicks=1, interval=0.0, button='left')
    time.sleep(6)

    #固定位置截图
    get_screen_info(imagefilepath)

    #图片识别保存
    pic_result = get_pic_text(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')

    #MD5 重复过滤
    judge_result(imagefilepath, pic_result)

    time.sleep(2) 

    #检查是否需要重启小程序
    restart_applet()

