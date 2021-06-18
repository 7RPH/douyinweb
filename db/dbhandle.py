#这是数据库操作部分的接口 请尽量返回字典或json
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='douyin')
cursor = db.cursor()

#性别比例需要数据形如[{name: '男', value: 10}, {name: '女', value: 10}, {name: '未知', value: 30}]

#视频点赞数需要数据形如[{name: '渗透测试', value: 播放量}],按照前十的播放量的从小往大的顺序返回

#