
import time

import baiduapi
import studysql
import printscreen

nowfile = "D:\\tupian\\1.jpg"

studysql.connect_db()

try:
    while(1):  
        time.sleep(2)
        haha =  printscreen.print_screen_and_return_result()
        if(haha):
            mystr = baiduapi.get_pic_text(nowfile)
            if(mystr != -1):
                studysql.find_db_and_return_result(mystr)
            else:
                print("不是正确图片!放弃!")  
                               
except KeyboardInterrupt:
    studysql.close_db()