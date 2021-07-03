import requests
import time
import json
class lover:
    headers={
        'Accept-Encoding': 'gzip',
        'X-SS-REQ-TICKET': '1624116409161',
        'sdk-version': '1',
        'Cookie': 'install_id=18059295469224; ttreq=1$5bcebc40af4ad7b149b0c27a2b97ea891751f0ef; passport_csrf_token_default=93b8a6d9cbbd1ac3b8fcc13775ec7ff2; odin_tt=be9ac91eb7d4a8d08b81e9ed5f681a6da413c84c079f22c5152d333f91df6297d0d409b85f855b23b2daee7001bb41f89912fca703224906bf0dd6eab87daf52; n_mh=CywfJH4yRULpgiQ43BETnrjz3bV22-_iiE_S7zw6JNM; sid_guard=92141b9d0fec3c3ce899cc5e77449443%7C1623990319%7C5184000%7CTue%2C+17-Aug-2021+04%3A25%3A19+GMT; uid_tt=5bce9504a7f8de289dff20328e2a61d5; sid_tt=92141b9d0fec3c3ce899cc5e77449443; sessionid=92141b9d0fec3c3ce899cc5e77449443; d_ticket=522f901d58deef85942de523391a1fcbbef2f; _ga=GA1.2.2033731185.1623990474; qh[360]=1',
        'x-tt-token': '0092141b9d0fec3c3ce899cc5e77449443053a1a47f1bbd23ac7ca6695c9ffda8b2ea9b9864ec5c747589cacb07b3d2b886f69171790c4b53f121ced17167834eff7a199117806e57c0a2974f00f80bc9790f6a1f7c2c96e9e2cf244db5d54dc630a5-1.0.1',
        'X-Gorgon': '03006cc0c400666a725ebb987e9261521082a5cbceb66749c5e4',
        'X-Khronos': '1624116409',
        'X-Pods': 'Host: aweme.snssdk.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.10.0.1',
    }

    sec_user_id="MS4wLjABAAAApYMdC_Siv8FRVovzWikksR91fms5BiH1iFU73Os1aBw"
    # url=f'https://hotsoon.snssdk.com/hotsoon/interact/relation/_followers/?count=30&from_db=false&current_user_id=MS4wLjABAAAAIA-eufxLBtHxtoAfDy9kcy614cDXvafqO0mvaDdXh70&max_time={ts+1000}&sort_type=time&aweme_not_auth_field=0&is_dy_domain=false&flt_pkg_name=host&flt_pkg_version=-1&live_sdk_version=110700&disable_recommend_strategy=0&iid=493043721181438&device_id=2726426916949527&ac=wifi&mac_address=0C%3ADD%3A24%3A04%3AC2%3AD9&channel=tengxun_1112_0531&aid=1112&app_name=live_stream&version_code=110700&version_name=11.7.0&device_platform=android&ssmix=a&device_type=MI+9&device_brand=Android&language=zh&os_api=22&os_version=5.1.1&uuid=863064706319425&openudid=622c1a52fbe290c3&manifest_version_code=110700&resolution=900*1600&dpi=320&update_version_code=11070004&_rticket=1623946749760&tab_mode=3&client_version_code=110700&jssdk_version=1.63.0.0&js_sdk_version=1.63.0.0&mcc_mnc=46007&hs_location_permission=1&cpu_support64=false&host_abi=armeabi-v7a&rom_version=XIAOMI_unknown&cdid=b09edf65-b058-4a9e-9aa3-ac369194a4d0&new_nav=0&screen_width=450&ws_status=ConnectionState%7BState%3D16%7D&settings_version=24&last_update_time=1623944034889&cpu_model=placeholder&ts={ts}'
    # offset=0

    def GetSec_uid(self,offset):
        '''
        返回粉丝加密的id,一次20个
        :param offset: 偏移量
        :return:
        '''
        sec_uidlist=[]
        # url=f"https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=17&max_time=1623990346&count=20&offset={offset}&source_type=1&address_book_access=1&gps_access=1&ts=1623990680&js_sdk_version=1.16.0.0&app_type=normal&os_api=22&device_type=MI%209&device_platform=android&ssmix=a&iid=18059295469224&manifest_version_code=630&dpi=320&uuid=863064706319425&version_code=630&app_name=aweme&version_name=6.3.0&openudid=622c1a52fbe290c3&device_id=2726426916949527&resolution=1600*900&os_version=5.1.1&language=zh&device_brand=Android&ac=wifi&update_version_code=6302&aid=1128&channel=wandoujia_aweme1&_rticket=1623990681797&mcc_mnc=46007&sec_user_id={self.sec_user_id}"
        url="https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=104255897823&max_time=1624116408&count=20&offset=20&source_type=1&address_book_access=1&gps_access=1&ts=1624116408&js_sdk_version=1.16.3.5&app_type=normal&os_api=22&device_type=MI%209&device_platform=android&ssmix=a&iid=18059295469224&manifest_version_code=630&dpi=320&uuid=863064706319425&version_code=630&app_name=aweme&version_name=6.3.0&openudid=622c1a52fbe290c3&device_id=2726426916949527&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&ac=wifi&update_version_code=6302&aid=1128&channel=wandoujia_aweme1&_rticket=1624116409162&mcc_mnc=46007&sec_user_id=MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4"
        response=requests.get(url=url,headers=self.headers).text
        print(response)
        json_list=json.loads(response)
        #加密id
        for i in range(0,20):
            sec_uid=json_list['followers'][i]['sec_uid']
            sec_uidlist.append(sec_uid)
        # print(sec_uidlist)
        return sec_uidlist

# l=lover()
# l.GetSec_uid(20)

'''
MS4wLjABAAAArLR296-wlY4FfpcMDAhvftQS-w_9gYsyUVQOmydcByE-_VqGXRbPc7SACBZblep6
MS4wLjABAAAArLR296-wlY4FfpcMDAhvftQS-w_9gYsyUVQOmydcByE-_VqGXRbPc7SACBZblep6
'''

'''
https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=104255897823&max_time=1624116385&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&ts=1624116959&js_sdk_version=1.16.3.5&app_type=normal&os_api=22&device_type=MI%209&device_platform=android&ssmix=a&iid=18059295469224&manifest_version_code=630&dpi=320&uuid=863064706319425&version_code=630&app_name=aweme&version_name=6.3.0&openudid=622c1a52fbe290c3&device_id=2726426916949527&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&ac=wifi&update_version_code=6302&aid=1128&channel=wandoujia_aweme1&_rticket=1624116960361&mcc_mnc=46007&sec_user_id=MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4
https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=104255897823&max_time=1624116408&count=20&offset=0&source_type=1&address_book_access=1&gps_access=1&ts=1624116408&js_sdk_version=1.16.3.5&app_type=normal&os_api=22&device_type=MI%209&device_platform=android&ssmix=a&iid=18059295469224&manifest_version_code=630&dpi=320&uuid=863064706319425&version_code=630&app_name=aweme&version_name=6.3.0&openudid=622c1a52fbe290c3&device_id=2726426916949527&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=Android&ac=wifi&update_version_code=6302&aid=1128&channel=wandoujia_aweme1&_rticket=1624116409162&mcc_mnc=46007&sec_user_id=MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4"

'''