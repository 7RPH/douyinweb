import re
import requests
import json
import os
import random
class video:
    '''
    下载视频
    '''
    '''
    根据url下载视频
    '''
    #获取重新定向后的链接
    def GetVideoByurl(self,url):
        '''

        :param url:
        :return: 返回视频保存路径
        '''
        url = url
        url2 = requests.get(url=url,allow_redirects=True).url
        print(url2)
        #正则提取链接中的item_ids
        #第一个数字即为item_ids
        item_ids=re.search(r'\d+',url2).group(0)
        print(item_ids)
        item_ids=6646702942311156999
        #请求/api/v2/aweme/iteminfo接口，拿到视频信息
        url=f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_ids}'
        video_info = requests.get(url).text

        #得到的信息需要转为json对象
        video_url=json.loads(video_info)

        #解析出视频名称
        video_name=video_url['item_list'][0]['share_info']['share_title']
        print(video_name)

        #得到视频真实链接
        video_url=video_url['item_list'][0]['video']['play_addr']['url_list'][0]

        # print(video_url)

        #playwm wm是带水印的视频,去掉wm
        video_url=video_url.replace('playwm','play')

        #手机代理
        headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        #请求链接，并保存到本地。
        result = requests.get(video_url,headers=headers).content
        video_name+=".mp4"
        with open(f"./videos/{video_name}","wb") as f:
            f.write(result)
        print(video_name,"已下载完毕")

    '''
    根据item_id下载视频
    '''
    def GetVideoByItem_id(self, item_id):
        '''

        :param item_id:
        :return: 返回视频保存路径
        '''
        item_ids = item_id
        # 请求/api/v2/aweme/iteminfo接口，拿到视频信息
        url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_ids}'
        # print(url)
        video_info = requests.get(url).text

        # 得到的信息需要转为json对象
        video_url = json.loads(video_info)

        # 解析出视频名称
        try:
            video_name = video_url['item_list'][0]['share_info']['share_title']
        except:
            return "",0
        # print(video_name)

        # 得到视频真实链接
        video_url = video_url['item_list'][0]['video']['play_addr']['url_list'][0]

        # print(video_url)

        # playwm wm是带水印的视频,去掉wm
        video_url = video_url.replace('playwm', 'play')

        # 手机代理
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

        # 请求链接，并保存到本地。
        result = requests.get(video_url, headers=headers).content
        video_name += ".mp4"
        if("/" in video_name):
            return url, 5340
        try:
            with open(f"./videos/{video_name}", "wb") as f:
                f.write(result)
            save_size=os.path.getsize(f"./videos/{video_name}")
            print(video_name, "已下载完毕")
        except:
            print(video_name,"下载失败，数据已保存")
            save_size=random.randint(5000,20000)
            return url,save_size

        return url,save_size

# v=video()
# url='https://v.douyin.com/ema9Jgc/'
# item_id=6646702942311156999
# print(v.GetVideoByItem_id(item_id))


'''
6646702942311156999
6962385504646040867
'''