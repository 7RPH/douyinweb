from fensi import lover
from time import sleep
import random
from  save import  savedata
basetime=60
l=lover()
sdata=savedata()
#获取粉丝加密id
#具体应用

for i in range(0,10000,20):
    encrypted_id = l.GetSec_uid(i)
    #save encrypted_id_list flag=0 <20条数据的数组>
    for eid in encrypted_id:
       ulist=['','1',eid,'0']
       sdata.save_id(ulist)
    #pass
    print(str(i),"条数据入库")
    sleep(random.randint(basetime-10,basetime+10))