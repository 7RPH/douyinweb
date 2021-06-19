# # 这是数据库操作部分的接口
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host='47.242.248.7',
#                      user='scu_douyin',
#                      password='JSs3EXHt5mGD5DPy',
#                      database='app')
# cursor = db.cursor()
#
#
# # 性别比例需要数据
# def getSex():
#     return {'sexdata': [{"name": "男", "value": 100}, {"name": "女", "value": 145}, {"name": "未知", "value": 14}]}
#
#
# # 视频点赞数,按照前十的播放量的从小往大的顺序返回
# def getLike():
#     return {'likename': ['乐色炸串', '乐色暑促', 'i春秋', 'ichunqiu', 'github', 'gitee', '渗透', '渗透测试', '测试', 'test'],
#             'likelist': sorted([114, 514, 191, 982, 11, 451, 419, 198, 101, 141])[::-1]}
#
#
# # 爬取到的2020年每个月份的视频数量
# def getNum():
#     return {'num': [114, 514, 191, 981, 11, 451, 419, 198, 101, 145, 141, 919]}


# 这是数据库操作部分的接口
import pymysql

# 打开数据库连接
db = pymysql.connect(host='47.242.248.7',
                     user='scu_douyin',
                     password='JSs3EXHt5mGD5DPy',
                     database='app')
cursor = db.cursor()


# 性别比例需要数据
def getSex():
    db.ping()
    sql1 = "SELECT COUNT(ugender) AS male FROM user where ugender='male'"
    sql2 = "SELECT COUNT(ugender) AS male FROM user where ugender='female'"
    sql3 = "SELECT COUNT(ugender) AS male FROM user where ugender='unknown'"

    try:
        cursor.execute(sql1)
        malenum = cursor.fetchall()
        cursor.execute(sql2)
        femalenum = cursor.fetchall()
        cursor.execute(sql3)
        unknownum = cursor.fetchall()
        return {'sexdata': [{"name": "男", "value": malenum[0][0]}, {"name": "女", "value": femalenum[0][0]},
                            {"name": "未知", "value": unknownum[0][0]}]}
    except:
        print("error")


# 视频点赞数,按照前十的播放量的从小往大的顺序返回
def getLike():
    db.ping()
    sql = "select vsummary,likenum from video order by likenum desc LIMIT 10"
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        likename = []
        likelist = []
        for ri in res:
            likename.append(ri[0])
            likelist.append(ri[1])
        responce = {'likename': likename, 'likelist': likelist}
        return responce
    except:
        print("error")


# 爬取到的2020年每个月份的视频数量
def getNum():
    db.ping()
    sql = "select putdate from video;"
    cursor.execute(sql)
    times = cursor.fetchall()
    res = [0] * 12
    for i in times:
        tmp = i[0].split('-')[:2]
        if tmp[0] == '2020':
            res[int(tmp[1]) - 1] += 1
    return {'num': res}


# 获得之前搜索的关键词
def getKeywords():
    filepath = r'keyword.txt'
    li = open(filepath, 'r', encoding='utf8').read().splitlines()
    res = []
    for i in li:
        if 'end' not in i:
            res.append(i)
    return {'tag': res}


# 修改爬取数据时用于搜索的关键词
def updateKeywords(keywords):  # keywords={'keywords':['key','word','s']}
    words = keywords['keywords']
    filepath = r'keyword.txt'
    # li = open(filepath, 'r', encoding='utf8').read().splitlines()
    # for i in words:
    #     if f'end {i}' in li:
    #         li[li.index(f'end {i}')]=li[i]
    #     elif i not in li:
    #         li.append(i)
    res = open(filepath, 'w', encoding='utf8')
    res.write('\n'.join(words))
    res.close()
    return True

# updateKeywords({'keywords':['i春秋','奇安信','四川大学','scu']})
print(getKeywords())