import pymysql
from searchbykey import search
from video_download import video
from upinfo import up
import setting
from time import sleep
import random


class savedata():

      def __init__(self):
          self.conn = pymysql.connect(host=setting.MYSQL_HOST, user=setting.MYSQL_USER,port=setting.MYSQL_PORT, password=setting.MYSQL_PASSWORD,database=setting.MYSQL_DB, charset='utf8')
          self.cursor = self.conn.cursor( )
          self.s = search()
          self.v= video()
          self.u = up()

      def searchAll(self,keyword,maxNum):
          self.video_info_dic, self.item_id_list, self.encrypted_id_list = self.s.SearchByKeyword(keyword, maxNum)
          i=0
          for videoinfo in self.video_info_dic.values():
              ipath,isize=self.v.GetVideoByItem_id(self.item_id_list[i])
              self.save_video(ipath, isize, videoinfo)
              sleep(random.randint(5,10))
              i=i+1

          for encrypted_id in self.encrypted_id_list:
              upInfo = self.u.GetUpInfo(encrypted_id)
              print(upInfo)
              print(upInfo[0])
              self.save_user(upInfo)


      def save_video(self,vinfo,vpath='',vsize=0,vkeyword='',vitemid=''):
          self.conn.ping()
          vsize=vsize/(1024*1024)
          svsize=("%.2f" % vsize)+"MB"
          sql='INSERT INTO `video` (`vpath`, `vsize`, `vsummary`, `putdate`, `uname`, `likenum`, `comnum`, `keyword`, `itemId`) VALUES (\'{t1}\', \'{t2}\', \'{t3}\', \'{t4}\', \'{t5}\', \'{t6}\', \'{t7}\', \'{t8}\', \'{t9}\');'.format(t1=vpath,t2=svsize,t3=vinfo[0],t4=vinfo[1],t5=vinfo[2],t6=int(vinfo[3]),t7=int(vinfo[4]),t8=vkeyword,t9=vitemid)
          try:
             self.cursor.execute(sql)
          except:
             print("error save_video")

      def save_user(self,upinfo):
          if upinfo[4]==0:
              upinfo[4]="unknown"
          elif upinfo[4]==1:
              upinfo[4]="male"
          elif upinfo[4]==2:
              upinfo[4]="female"
          sql="INSERT INTO `user` (`uname`, `userid`, `uphoto`, `uprof`, `ugender`, `getlike`, `getfan`, `follown`, `worknum`) VALUES (\'{t0}\',\'{t1}\', \'{t2}\', \'{t3}\', \'{t4}\', \'{t5}\', \'{t6}\', \'{t7}\', \'{t8}\');".format(t0=upinfo[0],t1=upinfo[1],t2=upinfo[2],t3=upinfo[3],t4=upinfo[4],t5=upinfo[5],t6=upinfo[6],t7=upinfo[7],t8=upinfo[8])
          try:
              self.cursor.execute(sql)
          except:
            print("error save_user")

      def save_id(self,idInfo):
          sql="INSERT INTO `useid` (`itemId`, `flagV`, `encrypId`, `flagU`) VALUES (\'{t0}\',\'{t1}\', \'{t2}\', \'{t3}\');".format(t0=idInfo[0],t1=int(idInfo[1]),t2=idInfo[2],t3=int(idInfo[3]))
          try:
            self.cursor.execute(sql)
          except:
            print("error save_id")

      def find_uid(self,backnum,siteId):
          sql="SELECT DISTINCT `encrypId` FROM `useid` WHERE `flagU` = 0 AND `id` > "+str(siteId)+" limit "+str(backnum)
          try:
            self.cursor.execute(sql)
            list=self.cursor.fetchall()
            rlist=[]
            for lis in list:
                rlist.append(lis[0])
            return rlist
          except:
            print("error find_uid")

      def find_vid(self,backnum):
          sql="SELECT DISTINCT `itemID` FROM `useid` WHERE `flagV` = 0 limit "+str(backnum);
          try:
            self.cursor.execute(sql)
            list=self.cursor.fetchall()
            rlist=[]
            for lis in list:
                rlist.append(lis[0])
            return rlist
          except:
            print("error find_vid")

      def mark_uid(self,uid):
          sql="UPDATE useid SET flagU = 1 WHERE encrypId = "+'\''+str(uid)+'\';'
          try:
            self.cursor.execute(sql)
          except:
            print("error mark_uid")

      def mark_vid(self,vid):
          sql="UPDATE useid SET flagV = 1 WHERE itemId = "+'\''+str(vid)+'\';'
          try:
            self.cursor.execute(sql)
          except:
            print("error mark_vid")

      def change_video(self,vpath,vsize,vid):
          vsize=vsize/(1024*1024)
          svsize=("%.2f" % vsize)+"MB"
          sql="UPDATE `video` SET `vpath` = "+'\''+vpath+'\''+", `vsize` = "+'\''+svsize+'\''+" WHERE `video`.`itemId` = "+'\''+vid+'\''+";"
          try:
            self.cursor.execute(sql)
          except:
            print("error change_video")

      def find_gennder(self):
          sql1="SELECT COUNT(ugender) AS male FROM user where ugender='male'"
          sql2="SELECT COUNT(ugender) AS male FROM user where ugender='female'"
          sql3="SELECT COUNT(ugender) AS male FROM user where ugender='unknown'"

          try:
            self.cursor.execute(sql1)
            malenum=self.cursor.fetchall()
            self.cursor.execute(sql2)
            femalenum=self.cursor.fetchall()
            self.cursor.execute(sql3)
            unknownum=self.cursor.fetchall()
            return  malenum[0][0],femalenum[0][0],unknownum[0][0]
          except:
            print("error find_gennder")

      def find_likenum(self):
          sql="select vsummary,likenum from video order by likenum desc LIMIT 10"
          try:
             self.cursor.execute(sql)
             list=self.cursor.fetchall()
             return list
          except:
              print("error find_likenum")

      def close(self):
          self.cursor.close()
          self.conn.close()

# st=savedata()
# st.searchAll(keyword="网络安全",maxNum=10)

# s=savedata()
# print(s.find_vid(10))
# print(s.find_uid(10))

# s.find_likenum()
