from searchbykey import search
from video_download import video
from time import sleep
import random
from save import savedata
s=search()

'''
使用案例
'''
# keywords=["网络空间安全","i春秋","奇安信"]
# keywords=["奇安信"]
#最多搜索结果数目,次数为10的倍数 10,20,30
MaxNum=80
#搜索偏移的时间间隔s
basetime=60
sdata=savedata()

def GetVideoinfo(keyword):
    video_info_dic,item_id_list,encrypted_id_list=s.SearchByKeyword(keyword,MaxNum,basetime)
    print("数据返回")

    i=0
    for videoinfo in video_info_dic.values():
        #视频信息保存
        sdata.save_video(vinfo=videoinfo,vitemid=item_id_list[i],vkeyword=keyword)
        useid = [item_id_list[i],0,encrypted_id_list[i],0]
        #视频ID、用户ID保存
        sdata.save_id(useid)
        i=i+1
    print(keyword,"入库成功")
    sleep(random.randint(basetime-6,basetime+6))



'''
keyword 调度
'''
def spider():
    keywordlist = []
    with open("./keyword.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for key in lines:
        if ("end" not in key):

            print("爬取", key)
            GetVideoinfo(key)
            keywordlist.append(key)
            print(key, "已爬取完成")

            # 保存状态
            try:
                with open("./keyword.txt", "w", encoding="utf-8") as f_w:
                    for line in lines:
                        if (line in keywordlist and "end" not in line):
                            f_w.write("end " + line)
                        else:
                            f_w.write(line)
            except:
                print("保存状态失败")
