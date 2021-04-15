
from PIL import ImageGrab # 屏幕截图
import win32gui # 窗口坐标获取
import win32api
import hashlib # MD5库


#全局变量
n = 0
imagefilepath = "D:\\tupian\\original_picture\\"
nowfilepath = "D:\\tupian\\"

picture_md5_list = []

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
    im = ImageGrab.grab(bbox=(left + 15 , top + 100, right -15, bottom -100))
    im.save(imagefilepath + ('0000' + str(n))[-4:] + '.jpg')
    im.save(nowfilepath + '1.jpg')  

# 获取图片MD5数值
def get_file_md5(file_name):
    with open(file_name, 'rb') as fp:
        data = fp.read()
    file_md5= hashlib.md5(data).hexdigest()
    return file_md5

# 分析图片的MD5数值，用于过滤重复
def analyse_picture_md5(picture_path):
    global n
    global picture_md5_list
    pic_md5 = get_file_md5(picture_path + ('0000' + str(n))[-4:] + '.jpg')

    if(pic_md5 in picture_md5_list):
        print("图片重复，放弃保存，QAQ ！")
        return 0
    else:
        picture_md5_list.append(pic_md5)
        return 1 

def print_screen_and_return_result():
    global imagefilepath

    left, top, right, bottom = get_small_app_coords()

    get_screen_info(imagefilepath, nowfilepath, left, top, right, bottom)

    return analyse_picture_md5(imagefilepath)
