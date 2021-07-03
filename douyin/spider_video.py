from video_download import video
from time import sleep
from save import  savedata
import random

v=video()
sdata=savedata()
basetime=30
SpiderNum=500
item_id_list=sdata.find_vid(SpiderNum)
#从数据库读取 item_id //flag=0
#适量数据即可
#pass

#下载视频
for item_id in item_id_list:
    #根据item_id
    url_path, size = v.GetVideoByItem_id(item_id)

    #save  url_path  视频url路径  size 视频大小
    sdata.change_video(vpath=url_path,vsize=size,vid=item_id)
    #pass

    #对应item_id flag置为1
    sdata.mark_vid(item_id)
    #pass

    sleep(random.randint(basetime-6,basetime+6))
