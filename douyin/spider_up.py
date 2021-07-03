from upinfo import up
from time import sleep
import random
from save import savedata
SpiderNum=100
basetime=50
u=up()
sdata=savedata()
location=12793
encrypted_id_list=sdata.find_uid(SpiderNum,location)
#读取 encrypted_id,数据适量即可
count=0
if __name__=="__main__":
    print("开始爬取用户")
    for encrypted_id in encrypted_id_list:
        #保存用户信息
        upInfo=u.GetUpInfo(encrypted_id)
        sdata.save_user(upInfo)

        #标记用户flag
        sdata.mark_uid(encrypted_id)
        count+=1
        # if(count%10==0):
        print("已爬取 "+str(count)+" 条用户数据")
        sleep(random.randint(basetime-6,basetime+6))