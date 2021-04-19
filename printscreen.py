
from PIL import ImageGrab # 屏幕截图
import win32gui # 窗口坐标获取
import win32api
import hashlib # MD5库
import os

#全局变量
n = 310
imagefilepath = "D:\\tupian\\original_picture\\"
nowfilepath = "D:\\tupian\\"
picture_md5_file = "D:\\tupian\\picture_md5.txt"

picture_md5_list = []

left = 0
top = 0 
right = 0
bottom = 0

# 获取小程序窗口坐标
def get_small_app_coords():
    titlename = "文化海康"
    hwnd = win32gui.FindWindow(None, titlename)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom

# 固定位置截图
def get_screen_info(imagefilepath, nowfilepath, left, top, right, bottom):
    global n
    n += 1
    im = ImageGrab.grab(bbox=(left + 15 , top + 150, right -15, bottom))
    im.save(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')
    im.save(nowfilepath + '1.jpg')  

# 获取图片MD5数值
def get_file_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5= hashlib.md5(data).hexdigest()
    return file_md5

# 将结果保存至指定文件中
def save_result_to_file(fliename ,result):  
    print(result)
    result += '\n'
    txt_file = open(fliename, 'a+', encoding='utf-8')
    txt_file.write(result)
    txt_file.close() 

# 分析图片的MD5数值，用于过滤重复
def analyse_picture_md5(picture_path):
    global n
    global picture_md5_file
    global picture_md5_list
    pic_md5 = get_file_md5(picture_path + ('0000' + str(n))[-4:] + '.jpg')

    if(pic_md5 in picture_md5_list):
        print("界面未更新!\n")
        os.remove(picture_path + ('0000' + str(n))[-4:] + '.jpg')
        return 0
    else:
        picture_md5_list.append(pic_md5)
        save_result_to_file(picture_md5_file , pic_md5)
        print("界面更新,进入下一步...")
        return 1 

def print_screen_and_return_result():
    global imagefilepath
    # global left, top, right, bottom
    # left, top, right, bottom = get_small_app_coords()
    #print(left, top, right, bottom)
    get_screen_info(imagefilepath, nowfilepath, left, top, right, bottom)

    return analyse_picture_md5(imagefilepath)

