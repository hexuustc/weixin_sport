# encoding=utf8
import requests
import datetime
import pytz
import argparse
import random

class Report(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def report(self):
        url = "http://cx.yydsq.cn/app/ajax.php?c=add"
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
        data = {
            'usr':self.user,
            'psw':self.password,
            'bs':step
        }
        ret = requests.post(url,data=data)
        status = ret.status_code
        print(status)
        if status==200:
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
    count = 2
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