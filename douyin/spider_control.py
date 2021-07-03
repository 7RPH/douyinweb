from fensi import lover
from upinfo import up
from time import sleep
import random
from  save import  savedata
from video_download import video


class scontrol():
    def __init__(self):
        self.basetime=10
        self.keywords=["网络空间安全", "i春秋", "奇安信"]
        self.MaxNum=10


    def spider_videoinfo(self):
        sdata = savedata()
        for keyword in self.keywords:
            video_info_dic, item_id_list, encrypted_id_list = s.SearchByKeyword(keyword, self.MaxNum, self.basetime)
            i = 0
            for videoinfo in video_info_dic.values():
                # 视频信息保存
                sdata.save_video(vinfo=videoinfo, vitemid=item_id_list[i], vkeyword=keyword)
                useid = [item_id_list[i], 0, encrypted_id_list[i], 0]
                # 视频ID、用户ID保存
                sdata.save_id(useid)
                i = i + 1
            sleep(random.randint(self.basetime - 3, self.basetime + 3))

    def spider_up(self):
        u = up()
        sdata = savedata()
        encrypted_id_list = sdata.find_uid(3*self.MaxNum)
        # 读取 encrypted_id,数据适量即可
        for encrypted_id in encrypted_id_list:
            # 保存用户信息
            upInfo = u.GetUpInfo(encrypted_id[0])
            sdata.save_user(upInfo)

            # 标记用户flag
            sdata.mark_uid(encrypted_id[1])

            sleep(random.randint(self.basetime-3,self.basetime+3))

    def spider_video(self):
        v = video()
        sdata = savedata()
        item_id_list = sdata.find_vid(2*self.MaxNum)
        # 从数据库读取 item_id //flag=0

        # 下载视频
        for item_id in item_id_list:
            # 根据item_id
            url_path, size = v.GetVideoByItem_id(item_id[0])

            # save  url_path  视频url路径  size 视频大小
            sdata.change_video(vpath=url_path, vsize=size, vid=item_id[0])
            # pass
            # 对应item_id flag置为1
            sdata.mark_vid(item_id[1])
            # pass
            sleep(random.randint(self.basetime - 3, self.basetime + 3))

    def spider_lover(self):
        l = lover()
        sdata = savedata()
        # 获取粉丝加密id
        # 具体应用
        for i in range(0, 10000, 20):
            encrypted_id = l.GetSec_uid(i)
            # save encrypted_id_list flag=0 <20条数据的数组>
            for eid in encrypted_id:
                ulist = ['', '1', eid, '0']
                sdata.save_id(ulist)
            # pass
            sleep(random.randint(self.basetime - 3, self.basetime + 3))