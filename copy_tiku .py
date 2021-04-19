
import time

import baiduapi
import studysql
import printscreen
import clickevent

nowfile = "D:\\tupian\\1.jpg"

file = open("D:\\tupian\\picture_md5.txt", 'r+')

while 1:
    line = file.readline()
    if not line:
        print("读取图片MD5并写入数组完毕！")
        break
    printscreen.picture_md5_list.append(line[:-1])

studysql.connect_db()

try:
    while 1:

        printscreen.left, printscreen.top, printscreen.right, printscreen.bottom = printscreen.get_small_app_coords()

        time.sleep(2)
        clickevent.click_exit()
        # print("退出小程序！")

        time.sleep(2)
        clickevent.click_entrance()
        # print("点击入口！")

        time.sleep(2)
        clickevent.click_into()
        # print("进入小程序！")

        time.sleep(2)
        clickevent.click_dati()
        # print("进入答题界面!")

        time.sleep(3)
        clickevent.click_start()
        print("进入答题!")

        time.sleep(3)
        haha = printscreen.print_screen_and_return_result()
        if(haha):
            mystr = baiduapi.get_pic_text(nowfile)
            if(mystr != -1):
                studysql.find_db_and_return_result(mystr)
            else:
                print("不是正确图片!放弃!\n")  
  
except KeyboardInterrupt:
    studysql.close_db()
