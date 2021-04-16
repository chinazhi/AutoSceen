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

# 解析图片文字 并拼接保存文字
def get_pic_text(filePath):  
    # 调用百度通用文字识别, 图片参数为本地图片 
    image = get_file_content(filePath)
    info = client.basicAccurate(image)
    
    #承接百度返回的数据
    nums = info['words_result_num']
    words_res = info['words_result']

    # 题目分区保存
    top_flag1 = '单选题'
    top_flag2 = '多选题'
    top_flag3 = '判断题'
    body_flag = 'A'
    result_flag = '正确答案'
    footer_flag = '奖励卡'
    top_words = ''
    body_words = ''
    result_words = ''
    first_word = ''

    # 类型 1 题目 2 选项 3 结果 
    words_type = 0  

    for i in range(nums):
        tmp = words_res[i]['words']
        #判断 文字类型
        if( (top_flag1 in tmp) or (top_flag2 in tmp) or (top_flag3 in tmp) ):
            words_type = 1
        elif ( (body_flag in tmp) ):
            words_type = 2
        elif( (result_flag in tmp) ):    
            words_type = 3
        elif( (footer_flag in tmp)):
            break    

        #保存文字到对应区域 
        if(words_type == 1):
            top_words += tmp
        elif(words_type == 2):
            body_words += tmp
        elif(words_type == 3):
            result_words += tmp    

    if(words_type == 0):
        print("未解析出任何关键字,返回-1")
        return -1

    first_word = words_res[1]['words']
    return {'first_word':first_word, 'top': top_words, 'body': body_words, 'result': result_words}

