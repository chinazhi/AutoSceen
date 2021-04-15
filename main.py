
import baiduapi
import studysql




mystr = baiduapi.get_pic_text('C:\\Users\\HK\\Desktop\\test\\2.png')

studysql.find_db_and_return_result(mystr)
