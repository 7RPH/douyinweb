import requests
import json
from up import up_extra
# url='https://v.douyin.com/eu63NJc/'
# url2=requests.get(url=url,allow_redirects=True).url
# url_302=url2.split('&')[1]
# print(url_302)
# sec_uid=url_302.split('=')[1]
# print(url_302)
class up:
    u=up_extra()
    def GetUpInfo(self,sec_uid):
        '''
        :param sec_uid:
        :return: 返回用户信息
        '''
        resultList=[]
        url=f'https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={sec_uid}'
        # print(url)
        up_info=requests.get(url=url).text
        up_json=json.loads(up_info)

        # 昵称
        nickname = up_json['user_info']['nickname']
        resultList.append(nickname)
        #抖音id
        id_douyin=up_json['user_info']['unique_id']
        if(id_douyin==""):
            id_douyin=up_json['user_info']['short_id']
        resultList.append(id_douyin)
        # 头像url
        ImageUrl = up_json['user_info']['avatar_medium']['uri']
        # https://p29.douyinpic.com/aweme/720x720/2fa6200078c02bf20af4d.jpeg
        ImageUrl = "https://p29.douyinpic.com/aweme/" + ImageUrl + ".jpeg"
        resultList.append(ImageUrl)
        #简介、签名
        signature=up_json['user_info']['signature']
        resultList.append(signature)
        #性别
        gender=self.u.GetSex(sec_uid)
        resultList.append(gender)
        # 获赞数
        total_favorited = int(up_json['user_info']['total_favorited'])
        resultList.append(total_favorited)
        # 粉丝数
        follower_count = up_json['user_info']['follower_count']
        resultList.append(follower_count)
        # up主的关注数
        following_count = up_json['user_info']['following_count']
        resultList.append(following_count)
        # 作品数
        aweme_count = up_json['user_info']['aweme_count']
        resultList.append(aweme_count)
        #喜欢数
        favoriting_count=up_json['user_info']['favoriting_count']
        # print(resultList)
        return resultList







# u=up()
# # sec_uid="MS4wLjABAAAAH3I-F_2XJVtQnbKfau-hVch_bwGnEea_m7-UwehM-8E"
# sec_uid="MS4wLjABAAAA5wkXZsrCqCRq4aPUmVE9DFvczq_EijqdCPuOPa5zAZg"
# t=u.GetUpInfo(sec_uid)
# print(t)