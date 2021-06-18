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
    return {'sexdata': [{"name": "男", "value": 1}, {"name": "女", "value": 145}, {"name": "未知", "value": 14}]}


# 视频点赞数,按照前十的播放量的从小往大的顺序返回
def getLike():
    return {'likename': ['乐色炸串', '乐色暑促', 'i春秋', 'ichunqiu', 'github', 'gitee', '渗透', '渗透测试', '测试', 'test'],
            'likelist': sorted([114, 514, 191, 982, 11, 451, 419, 198, 101, 141])}


# 爬取到的2020年每个月份的视频数量
def getNum():
    return {'num': [114, 514, 191, 981, 11, 451, 419, 198, 101, 145, 141, 919]}
