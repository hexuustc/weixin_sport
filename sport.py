# encoding=utf8
import requests
import datetime
import pytz
import argparse
import random
import json

class Report(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def report(self):
        url = "https://xzdx.xyz/x/ym/yzmb/api.php"
        timenow = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
        print(timenow.hour)
        if timenow.hour<=8 and timenow.hour>=7:
            step = random.randint(1000,1500)
        elif timenow.hour<=12 and timenow.hour>=11:
            step = random.randint(2000,2500)
        elif timenow.hour<=18 and timenow.hour>=17:
            step = random.randint(4000,4500) 
        elif timenow.hour<=23 and timenow.hour>=22:
            step = random.randint(6000,7000) 
        else:
            step = random.randint(1500,2000)
        step = 2218
        headers = {
            'authority': 'xzdx.xyz',
            'method': 'POST',
            'path': '/x/ym/yzmb/api.php',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-length': '48',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://xzdx.xyz',
            'referer': 'https://xzdx.xyz/x/ym/yzmb/',
            'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
            'x-requesteded-with':'XMLHttpRequest'
        }
        data = {
            'user':self.user,
            'password':self.password,
            'steps':step
        }
        ret = requests.post(url,data=data,headers=headers)
        status = ret.status_code
        string = ret.content.decode('UTF-8')
        json_message = json.loads(string)
        code = json_message['code']
        print(status)
        print(string)
        print(code)
        if status==200 and code=='200':
            print("Sport Success!")
            return True
        else:
            print("Sport Failed!")
            return False
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='weixin auto sport script.')
    parser.add_argument('user', help='your user name', type=str)
    parser.add_argument('password', help='your password', type=str)
    args = parser.parse_args()
    autorepoter = Report(user=args.user, password=args.password)
    count = 3
    while count != 0:
        ret = autorepoter.report()
        if ret != False:
            break
        print("Sport Failed, retry...")
        count = count - 1
    if count != 0:
        exit(0)
    else:
        exit(-1)