import requests
from TikTokApi import TikTokApi
import requests
import json


class ReadTiktok:
    def __init__(self):
        self.users = []
        self.tiktok = TikTokApi()

		# without slash as tail
        self.url = 'https://tiktoktsu.com'
        self.s_v_web_id = "verify_bece2d7e4e834299470ba7988111b513"

    def get_trending_data(self):
        try:
            trendingInfo = self.tiktok.by_trending(
                count=30, custom_verifyFp=self.s_v_web_id)
            if len(trendingInfo) != 0:
                url = self.url + "/api/rest/savetrending"
                payload = {
                    'data': json.dumps(trendingInfo)
                }
                headers = {}
                response = requests.request(
                    "POST", url, headers=headers, data=payload)

                print(response.text)
            pass
        except Exception as e:
            print(str(e))
            pass

    def read_users_from_server(self):
        response = requests.get(self.url + '/api/rest/getusers')

        print(response.status_code)
        if response.status_code == 200:
            self.users = response.json()
            for user in self.users:
                try:
                    print('sending request with {0}'.format(user['uniqueId']))
                    userInfo = self.tiktok.get_user(user['uniqueId'], custom_verifyFp="verify_bece2d7e4e834299470ba7988111b513")
                    if userInfo['serverCode'] == 200:
                        avatar = userInfo['userInfo']['user']['avatarThumb']
                        nickname = userInfo['userInfo']['user']['nickname']
                        follercount = userInfo['userInfo']['stats']['followerCount']
                        followingcount = userInfo['userInfo']['stats']['followingCount']
                        diggcount = userInfo['userInfo']['stats']['diggCount']
                        heart = userInfo['userInfo']['stats']['heart']
                        videocount = userInfo['userInfo']['stats']['videoCount']
                        signature = userInfo['userInfo']['user']['signature']
                        user_id = user['id']

                        url = self.url + "/api/rest/saveuser"

                        payload = {
                            'id': user['id'],
                            'avatar': avatar,
                            'uniqueId': user['uniqueId'],
                            'nickname': nickname,
                            'follercount': follercount,
                            'followingcount': followingcount,
                            'diggcount': diggcount,
                            'heart': heart,
                            'videocount': videocount,
                            'signature': signature
                        }
                        headers = {}

                        response = requests.request(
                            "POST", url, headers=headers, data=payload)

                        print(response.text)
                    else:
                        print(userInfo.text())
                except Exception as e:
                    print(str(e))
                    pass

        else:
            print(response.text())

    def read_users_from_server_test(self):
        userInfo = self.tiktok.get_user('neoneo', custom_verifyFp="verify_bece2d7e4e834299470ba7988111b513")
        print(json.dumps(userInfo, indent=4))

if __name__ == '__main__':
    tiktok_app = ReadTiktok()
    tiktok_app.read_users_from_server()
    tiktok_app.get_trending_data()

    # tiktok_app.read_users_from_server_test()
    
