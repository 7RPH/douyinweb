import time
import brotli
import requests
import json
from urllib import parse
import re
import datetime
from time import sleep
import random


class search:

    def clone(li1):
        li_copy = []
        li_copy.extend(li1)
        return li_copy

    def SearchByKeyword(self, keyword, MaxNum, basetime):
        '''
        每次搜索返回10个结果(如果够10个的话)
        :param keyword: 搜索关键词
        :return:  视频信息、Item_id_list(用于下载视频)、encrypted_id_list(用于爬取用户)
        '''

        query = parse.quote(keyword)
        offset = 0
        # url='https://hotsoon.snssdk.com/hotsoon/general_search/?query={query}&count=10&search_id&user_action=Initiative&click_rectify_bar=0&offset={offset}&search_type=0&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863064706319425&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=900*1600&dpi=320&update_version_code=11070004&_rticket=1622867693544&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=7061a471-d3ce-4a80-9323-beb389eb40a2&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1622867439277&cpu_model=placeholder&ts={ts} HTTP/1.1'.format(offset=offset,query=query,ts=ts)
        # print(url)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'odin_tt=6304a7495bc456b6f891b2b8a54f05a2715ebddbbd5d8e206810614a4e468d54c409ad3105e30676975f45fa0f7a074a32035314bc2ac926fea5c9b4105ce8e669c7b0553ef6be95957ee33bede1dd43',
            'Host': 'hotsoon.snssdk.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
        # videoinfo=requests.get(url=url,headers=headers).text
        # print(videoinfo)
        # videoinfo=json.loads(videoinfo)
        location = 0
        item_id_list = []
        encrypted_id_list = []
        videoInfoList = []
        videoDic = {}
        countNum = 0
        # 最多搜索数目
        MAX = MaxNum
        for offset_num in range(0, MAX, 10):
            ts = int(time.time())
            offset = offset_num
            # query、offset、ts
            # url=  'https://hotsoon.snssdk.com/hotsoon/general_search/?query={query}&count=10&search_id&user_action=Initiative&click_rectify_bar=0&offset={offset}&search_type=2&live_sdk_version=110700&disable_recommend_strategy=0&iid=4433693546149965&device_id=3659627030393821&ac=wifi&mac_address=6e%3A9f%3A01%3A2c%3A3b%3A57&channel=live_tengxun_wzl_0518&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=LENOVO+L79031&device_brand=LENOVO&language=zh&os_api=25&os_version=7.1.2&uuid=867141328091578&openudid=64b110c0cd436af1&manifest_version_code=110700&resolution=720*1280&dpi=240&update_version_code=11070004&_rticket=1622904364602&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46000&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=LENOVO_unknown&cdid=3a6c0427-53a3-48ad-8c0b-20aa01c392c4&new_nav=0&screen_width=480&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1622904359915&cpu_model=placeholder&ts={ts}'.format(offset=offset, query=query,ts=ts)
            url = 'https://hotsoon.snssdk.com/hotsoon/general_search/?query={query}&count=10&search_id&user_action=Initiative&click_rectify_bar=0&offset={offset}&search_type=0&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=LIO-AN00&device_brand=HUAWEI&language=zh&os_api=22&os_version=5.1.1&uuid=863064545019426&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=1600*900&dpi=320&update_version_code=11070004&_rticket=1625315515282&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=b09edf65-b058-4a9e-9aa3-ac369194a4d0&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1625315339165&cpu_model=placeholder&ts={ts}'.format(
                offset=offset, query=query, ts=ts)
            # url = 'https://hotsoon.snssdk.com/hotsoon/general_search/?query={query}&count=10&search_id&user_action=Initiative&click_rectify_bar=0&offset={offset}&search_type=0&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863064706319425&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=900*1600&dpi=320&update_version_code=11070004&_rticket=1622867693544&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=7061a471-d3ce-4a80-9323-beb389eb40a2&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1622867439277&cpu_model=placeholder&ts={ts} HTTP/1.1'.format(offset=offset, query=query,ts=ts)
            # print(url)
            videoinfo = requests.get(url=url, headers=headers)
            videoinfo = videoinfo.text
            # print(videoinfo)
            videoinfo = json.loads(videoinfo)
            for i in range(0, 4):
                try:
                    t = videoinfo['data'][i]['item_result']
                    location = i
                except:
                    pass
            for index in range(0, 10):
                try:
                    # 视频简介
                    description = videoinfo['data'][location]['item_result']['items'][index]['item']['description']
                    videoInfoList.append(description)
                    # 发布时间
                    create_time = videoinfo['data'][location]['item_result']['items'][index]['item']['create_time']
                    create_time = datetime.datetime.fromtimestamp(create_time)
                    videoInfoList.append(create_time)
                    # 发布者昵称
                    nickname = videoinfo['data'][location]['item_result']['items'][index]['item']['author']['nickname']
                    videoInfoList.append(nickname)
                    # 点赞数
                    digg_count = videoinfo['data'][location]['item_result']['items'][index]['item']['stats'][
                        'digg_count']
                    videoInfoList.append(digg_count)
                    # 评论数
                    comment_count = videoinfo['data'][location]['item_result']['items'][index]['item']['stats'][
                        'comment_count']
                    videoInfoList.append(comment_count)
                    # #转发数
                    # share_count=videoinfo['data'][location]['item_result']['items'][index]['item']['stats']['share_count']
                    # item_id
                    item_id = int(videoinfo['data'][location]['item_result']['items'][index]['item']['id_str'])
                    # 抖音加密id
                    encrypted_id = videoinfo['data'][location]['item_result']['items'][index]['item']['author'][
                        'encrypted_id']

                    item_id_list.append(item_id)
                    encrypted_id_list.append(encrypted_id)
                    temp = []
                    temp = videoInfoList[:]
                    videoDic[countNum] = temp
                    videoInfoList.clear()
                    countNum += 1
                except:
                    print('------------------------------------------------------------------\n暂无结果、爬取结束')
                    print("共爬取" + str(len(item_id_list)) + "条")
                    return videoDic, item_id_list, encrypted_id_list

                # print(description,create_time,nickname,digg_count,comment_count,item_id,encrypted_id)
            yield f'{keyword}  已爬取{str(int((offset / 10 + 1) * 10))}条数据'
            SleepTime = random.randint(basetime - 6, basetime + 6)
            sleep(SleepTime)

        return videoDic, item_id_list, encrypted_id_list


# s=search()
# v,i,e=s.SearchByKeyword("王冰冰",30,10)
# print(v)
# print(i)
# print(e)
# 参数
'''
https://hotsoon.snssdk.com/hotsoon/general_search/?query=%E5%88%BA%E5%AE%A2%E4%BC%8D%E5%85%AD%E4%B8%83
&count=10&search_id&user_action=Initiative&click_rectify_bar=0&offset=0&search_type=0
&live_sdk_version=110700&disable_recommend_strategy=0
&iid=493043721181438&device_id=2726426916949527
&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9
&channel=tengxun_1112_0531&aid=1112
&app_name=live_stream&version_code=110700&version_name=11.7.0
&device_platform=android&ssmix=a&device_type=VOG-AL10
&device_brand=Android&language=zh&os_api=22
&os_version=5.1.1&uuid=863064706319425
&openudid=622c1a52fbe290c3&manifest_version_code=110700
&resolution=900*1600&dpi=320&update_version_code=11070004
&_rticket=1622867693544&tab_mode=3&client_version_code=110700
&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007
&hs_location_permission=1&cpu_support64=false
&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown
&cdid=7061a471-d3ce-4a80-9323-beb389eb40a2
&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D
&settings_version=24&last_update_time=1622867439277&cpu_model=placeholder&ts=1622867693 HTTP/1.1


'''

# url
'''
GET /hotsoon/general_search/?query=%E7%BD%91%E7%BB%9C%E7%A9%BA%E9%97%B4%E5%AE%89%E5%85%A8&count=10&search_id=202106051919150102121831694D7BCBC2&user_action=Initiative&click_rectify_bar=0&offset=10&search_type=0&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863064706319425&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=1600*900&dpi=320&update_version_code=11070004&_rticket=1622891980900&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=7061a471-d3ce-4a80-9323-beb389eb40a2&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1622891937304&cpu_model=placeholder&ts=1622891980 HTTP/1.1
GET /hotsoon/general_search/?query=%E7%BD%91%E7%BB%9C%E7%A9%BA%E9%97%B4%E5%AE%89%E5%85%A8&count=10&search_id=202106051919150102121831694D7BCBC2&user_action=Initiative&click_rectify_bar=0&offset=20&search_type=0&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=VOG-AL10&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863064706319425&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=1600*900&dpi=320&update_version_code=11070004&_rticket=1622891985654&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=7061a471-d3ce-4a80-9323-beb389eb40a2&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1622891937304&cpu_model=placeholder&ts=1622891985 HTTP/1.1
'''
