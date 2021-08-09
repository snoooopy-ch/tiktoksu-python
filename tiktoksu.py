import requests
from TikTokApi import TikTokApi
import requests
import json


class ReadTiktok:
    def __init__(self):
        self.users = []
        self.tiktok = TikTokApi()

    def read_users_from_server(self):
        response = requests.get('https://tiktok.sakura.tv/api/rest/getusers')

        print(response.status_code)
        if response.status_code == 200:
            self.users = response.json()
            for user in self.users:
                try:
                    print('sending request with {0}'.format(user['uniqueId']))
                    userInfo = self.tiktok.get_user(user['uniqueId'])
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

                        url = "https://tiktok.sakura.tv/api/rest/saveuser"

                        # "?id={0}&avatar={1}&uniqueId={2}&nickname={3}&follercount={4}&followingcount={5}&diggcount={6}&heart={7}&videocount={8}&signature={9}"
                        # url = url.format(user['id'], avatar, user['uniqueId'], nickname,
                        #                  follercount, followingcount, diggcount, heart, videocount, signature)
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


if __name__ == '__main__':
    tiktok_app = ReadTiktok()
    tiktok_app.read_users_from_server()
