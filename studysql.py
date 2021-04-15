
import time  
import pymysql


# 搜索数据库题目列
def find_top_in_db(sqldb, sqlcur, param):
    sql = "select * from title WHERE top LIKE '%" + param + "%'"
    try:
        # 使用 execute()  方法执行 SQL 查询
        sqlcur.execute(sql)
        # 使用 fetchall() 方法获取查询结果
        data = sqlcur.fetchall()
        return data
    except :
        print("查询失败")
        return []

# 插入操作
def insert(sqldb, sqlcur, param):
    sql = "insert into title(time, top, body, result) values(%s, %s, %s, %s)"
    try:
        sqlcur.execute(sql, param)
        #提交
        sqldb.commit()
    except Exception as e:
        print("错误信息：%s" % str(e))
        # 错误回滚
        sqldb.rollback()

# 删除操作
def delete_top_in_db(sqldb, sqlcur):
    try:
        sqlcur.execute("delete from title where top='题目啊'")  # 执行
        # 提交
        sqldb.commit()
    except Exception as e:
        print("操作异常：%s" % str(e))
        # 错误回滚
        sqldb.rollback()

# 向指定数据库搜索，若无则写入，若有则显示
def find_db_and_return_result(api_str):
    # 打开数据库连接
    db = pymysql.connect(host='47.101.31.29', port=3306, user='tiku', passwd='tiku1708.', db='tiku')

    # 使用 cursor() 方法创建一个游标对象cur  查询结果以字典格式输出
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)

    find_db_result = find_top_in_db(db, cur, api_str['first_word'])

    if(len(find_db_result) > 0 ):
        print(find_db_result)
    else:
        insert(db, cur, (int(time.time()), api_str['top'], api_str['body'], api_str['result']))
        print("数据库中无此题目，写入数据库!")

    # 关闭数据库连接
    db.close()
