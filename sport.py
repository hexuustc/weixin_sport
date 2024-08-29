# encoding=utf8
import requests
import datetime
import pytz
import argparse
import random
import json
import urllib3

class Report(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def report(self):
        url = "https://api.kit9.cn/api/xiaomi_sports/api_email_fixed.php"
        timenow = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
        print(timenow.hour)
        if timenow.hour<=10 and timenow.hour>=7:
            step = random.randint(2000,3000)
        elif timenow.hour<=12 and timenow.hour>=11:
            step = random.randint(4000,5000)
        elif timenow.hour<=18 and timenow.hour>=17:
            step = random.randint(8000,9000) 
        elif timenow.hour<=23 and timenow.hour>=22:
            step = random.randint(10000,12000) 
        else:
            step = random.randint(1800,2000)
            #step = 3565
        headers = {
            'authority': 'api.kit9.cn',
            'method': 'POST',
            'path': '/api/xiaomi_sports/api_email_fixed.php',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-length': '56',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'http://shuabu.wang',
            'referer': 'http://shuabu.wang',
            'sec-ch-ua': '"Chromium";v="110", "Microsoft Edge";v="110", ";"Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
            'x-requesteded-with':'XMLHttpRequest'
        }
        data = {
            'email':self.user,
            'password':self.password,
            'step':step
        }
        # print("user: "+ self.user)
        # print("password: "+ self.password)
        ret = requests.post(url,data=data,headers=headers,verify=False)
        status = ret.status_code
        string = ret.content.decode('UTF-8')
        json_message = json.loads(string)
        code = json_message['code']
        print(status)
        print(string)
        print(code)
        if status==200 and code==200:
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
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
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