
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

# 全局变量
n = 0
picture_md5_list = []
imagefilepath = "D:\\jietu\\picture\\"
picture_md5_file = "D:\\jietu\\picture_md5.txt"

# 读取图片 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 获取图片MD5数值
def get_file_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5= hashlib.md5(data).hexdigest()
    return file_md5

# 固定位置截图
def get_screen_info(imagefilepath):
    global n
    n += 1
    im = ImageGrab.grab(bbox=(752, 303, 1165, 900))
    im.save(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')

# 将结果保存至指定文件中
def save_result_to_file(fliename ,result):  
    result += '\n'
    txt_file = open(fliename, 'a+', encoding='utf-8')
    txt_file.write(result)
    txt_file.close()
    print(result) 

# 分析图片的MD5数值，用于过滤重复
def analyse_picture_md5(picture_path):
    global n
    global picture_md5_file
    global picture_md5_list
    pic_md5 = get_file_md5(picture_path)
    image = get_file_content(picture_path)
    mystr = client.basicAccurate(image)
    print(mystr)

    if(pic_md5 in picture_md5_list):
        print("图片重复，放弃保存，QAQ ！")
        # 删除文件，可使用以下两种方法。
        os.remove(picture_path)
        return 0
    else:
        print("图片不同，保存图片，QAQ ！")
        picture_md5_list.append(pic_md5)
        save_result_to_file(picture_md5_file , pic_md5)
        return 1 

while 1:
    time.sleep(5)
    get_screen_info(imagefilepath)
    analyse_picture_md5(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')