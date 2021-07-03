import requests
import time
import json

class up_extra:
        timestamp=time.time()
        ts=int(timestamp)
        ts2=int(timestamp*1000)
        headers={
                'Accept-Encoding': 'gzip',
                'X-SS-REQ-TICKET': str(ts2),
                'passport-sdk-version': '21',
                'X-Tt-Token': '00ce70c68ca1e9450b5381b70a0a5bcfe6003c99cb980353462cad25d2dd9c292c8d7e26f32b41d0ece5fbdca33a3fe4e56f6f63994008feda956e4596d7e0940a735e0660aae4d4e51a07fe6cb628dc3f8d214a8ee082d676f65986f7177a32a995e-1.0.1',
                'sdk-version': '2',
                'Cookie': 'install_id=493043721181438; ttreq=1$a12edd2e49ae3161ccadc5b5e8c4b13f11b6808f; passport_csrf_token_default=b248c95afd219b1991704dadba012ca2; passport_csrf_token=b248c95afd219b1991704dadba012ca2; multi_sids=3043910695263374%3Ace70c68ca1e9450b5381b70a0a5bcfe6; n_mh=CywfJH4yRULpgiQ43BETnrjz3bV22-_iiE_S7zw6JNM; sid_guard=ce70c68ca1e9450b5381b70a0a5bcfe6%7C1623943490%7C5184000%7CMon%2C+16-Aug-2021+15%3A24%3A50+GMT; uid_tt=322223a3b96d6e31dc234cfaadd86db8; uid_tt_ss=322223a3b96d6e31dc234cfaadd86db8; sid_tt=ce70c68ca1e9450b5381b70a0a5bcfe6; sessionid=ce70c68ca1e9450b5381b70a0a5bcfe6; sessionid_ss=ce70c68ca1e9450b5381b70a0a5bcfe6; d_ticket=94af8d6431b878b88c17a4836b50b90cbef2f; odin_tt=57b1e1b49359b790a6baa19f97dfdcdadc8f7b3f604244e4a958fdf28088e56cb6dececaf2863e961d54ca82edda7a68524b21cf59629cc3feff3c5944579073ab368d7399d00d62e9ae7c050ad73ebf',
                'X-Ladon': 'qqu+PDB/l8rsXwOe3PYp66L2JzyzB6mZ+gAKrVp7JEaMFU7p',
                'X-Khronos': str(ts),
                'X-Gorgon': '040440880001c4c23cd31f9b3adf4b3f8d1bb8006555a38f7d04',
                'X-Tyhon': '03q40ZKKqdeIgq3fna2P8bSho//sr7T75K7LMi4=',
                'X-Argus': '5sHpM1VYDsnJcHCFk785BZ7pR71lB64jw3026kV29Bo72urWP4mpEc79NNMPwtatNls04J8iP6bzYFLmA1Am7LkhAPwtfWijGoESsANQIDxLYEDKcTYnZ7/7Fe9BCCVphv/eHEsnx4Fm6QJexQv8AE+bM5ooE7uO8wlhLlNy1ze6DAOKHbeR/CYknrjMU5QCNqp+9/aT9Qmf8w5e5IhihN4ltxLUU1rAEgvV0Ss8WAKRBRHDvEUfv82Yi/mZMKrOI+bXJaVZNkWUeKb0KZDW3huc',
                'Host': 'hotsoon.snssdk.com',
                'Connection': 'Keep-Alive',
                'User-Agent': 'okhttp/3.10.0.1',
                }
        ts=int(time.time())

        def GetSex(self,to_user_id):
                '''

                :param to_user_id:
                :return: 返回性别
                '''
                # to_user_id='MS4wLjABAAAAoOgvs6BOmt6S6LsZ5v7tQaqRlLczPsKRl26OKjvkwMk'
                to_user_id=to_user_id
                #to_user_id、ts
                # url=f'https://hotsoon.snssdk.com/hotsoon/user/profile/_get_profile/?to_user_id={to_user_id}&live_sdk_version=110700&disable_recommend_strategy=0&iid=2991138498168280&device_id=3659627030393821&ac=wifi&mac_address=6e%3A9f%3A01%3A2c%3A3b%3A57&channel=lephone_1112_1&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=LENOVO+L79031&device_brand=LENOVO&language=zh&os_api=25&os_version=7.1.2&uuid=867141328091578&openudid=64b110c0cd436af1&manifest_version_code=110700&resolution=720*1280&dpi=240&update_version_code=11070004&_rticket=1623931965523&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46000&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=LENOVO_unknown&cdid=5543c92d-7da6-43b6-b94f-10697b3a6e4e&new_nav=0&screen_width=480&ws_status=ConnectionState%7BState%3D4%7D&settings_version=24&last_update_time=1623931754064&cpu_model=placeholder&ts={self.ts}'
                url=f'https://hotsoon.snssdk.com/hotsoon/user/profile/_get_profile/?to_user_id={to_user_id}&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=LIO-AN00&device_brand=HUAWEI&language=zh&os_api=22&os_version=5.1.1&uuid=863064545019426&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=1600*900&dpi=320&update_version_code=11070004&_rticket=1625316011940&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=HUAWEI_unknown&cdid=b09edf65-b058-4a9e-9aa3-ac369194a4d0&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1625315339165&cpu_model=placeholder&ts={self.ts}'
                # print(url)
                upinfo=requests.get(url=url,headers=self.headers).text
                # print(upinfo)
                upinfo=json.loads(upinfo)
                #用户性别
                try:
                        gender=upinfo['data']['gender']
                except:
                        gender = 0
                return gender

# u=up_extra()
# # to_user_id='MS4wLjABAAAAoOgvs6BOmt6S6LsZ5v7tQaqRlLczPsKRl26OKjvkwMk'
# to_user_id='MS4wLjABAAAA5wkXZsrCqCRq4aPUmVE9DFvczq_EijqdCPuOPa5zAZg'
# a=u.GetSex(to_user_id)
# print(a)


