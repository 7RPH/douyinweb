from searchbykey import search
from video_download import video
from upinfo import up
from fensi import lover
from time import sleep
import random
s=search()
v=video()
u=up()
l=lover()

'''
使用案例
'''
keyword="网络空间安全"
#最多搜索结果数目,次数为10的倍数 10,20,30
MaxNum=20
#搜索偏移的时间间隔 s
basetime=15
video_info_dic,item_id_list,encrypted_id_list=s.SearchByKeyword(keyword,MaxNum,basetime)

#视频信息
# for videoInfo in video_info_dic.values():
#     #save videoInfo
#     print(videoInfo)

#下载视频
# for id in item_id_list:
#     url_path,size=v.GetVideoByItem_id(id)
#     #save  url_path  视频url路径  size 视频大小
#     print(url_path,size)
#     sleep(random.randint(10,15))



#用户信息
# for encrypted_id in encrypted_id_list:
#     upInfo=u.GetUpInfo(encrypted_id)
#     print(upInfo)
#     #save upInfo
#     #sleep(random.randint(10,15))



'''
粉丝加密id获取
一次返回20条数据的数组
'''
#偏移量 20为基数 [0,20,40,60]
# offset=40
# encrypted_id=l.GetSec_uid(offset)
# print(encrypted_id)
#具体应用
# for i in range(0,10000,20):
#     encrypted_id = l.GetSec_uid(i)
#     #save
#     sleep(random.randint(10,15))
