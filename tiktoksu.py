import requests
from TikTokApi import TikTokApi
import requests
import json


class ReadTiktok:
    def __init__(self):
        self.users = []
        self.tiktok = TikTokApi()

    def read_users_from_server(self):
        response = requests.get('http://192.168.3.66:8001/api/rest/getusers')

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
                        tiktok_id = userInfo['userInfo']['user']['id']
                        follercount = userInfo['userInfo']['stats']['followerCount']
                        followingcount = userInfo['userInfo']['stats']['followingCount']
                        diggcount = userInfo['userInfo']['stats']['diggCount']
                        heart = userInfo['userInfo']['stats']['heart']
                        videocount = userInfo['userInfo']['stats']['videoCount']

                        url = "http://192.168.3.66:8001/api/rest/saveuser"

                        "?id={0}&avatar={1}&tiktok_id={2}&uniqueId={3}&nickname={4}&follercount={5}&followingcount={6}&diggcount={7}&heart={8}&videocount={9}"
                        url = url.format(user['id'], avatar, tiktok_id, user['uniqueId'], nickname,
                                         follercount, followingcount, diggcount, heart, videocount)
                        payload = {
                            'id': user['id'],
                            'avatar': avatar,
                            'tiktok_id': tiktok_id,
                            'uniqueId': user['uniqueId'],
                            'nickname': nickname,
                            'follercount': follercount,
                            'followingcount': followingcount,
                            'diggcount': diggcount,
                            'heart': heart,
                            'videocount': videocount
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
