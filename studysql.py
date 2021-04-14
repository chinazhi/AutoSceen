import pymysql

from aip import AipOcr 

# 百度OCR APPID AK SK 
APP_ID = '23956565'
API_KEY = 'NvEtcxo3GlkYYT0doWsawKz7'
SECRET_KEY = 'ZYpY4fnBjhyX605ZPP6VOMCY38TeyTG6'
# 连接百度OCR
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片 
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('C:\\Users\\HK\\Desktop\\test\\2.png')
mystr = client.basicAccurate(image)
print(mystr)


# 打开数据库连接
db = pymysql.connect(host='47.101.31.29', port=3306, user='tiku', passwd='tiku1708.', db='tiku')

# 使用 cursor() 方法创建一个游标对象cur
cur = db.cursor()

# # 插入操作
# try:
#     cur.execute("insert into title(time, top, body, result) values(1, '题目', '选项', '答案')")
#     #提交
#     db.commit()
# except Exception as e:
#     print("错误信息：%s" % str(e))
#     # 错误回滚
#     db.rollback()

# 使用 execute()  方法执行 SQL 查询
# cur.execute("select top from title")

cur.execute("select * from title WHERE top LIKE '%题%'")

# 使用 fetchall() 方法获取查询结果
data = cur.fetchall()
print(data)

# 关闭数据库连接
db.close()
