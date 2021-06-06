#Bilibili爬虫
import requests
import time
import os

while True:
    os.system("clear")
    print("本次查询时间为: %s"%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print("请输入你要查询的UP主的UID: ",end="")
    upuid=str(input())    #你要查询的UP主的UID

    url_fans="https://api.bilibili.com/x/relation/stat?vmid="+upuid+"&jsonp=jsonp"
    url_power="https://api.bilibili.com/x/ugcpay-rank/elec/month/up?up_mid="+upuid
    url_info="https://api.bilibili.com/x/space/acc/info?mid="+upuid+"&jsonp=jsonp"
    url_video="https://api.bilibili.com/x/space/arc/search?mid="+upuid+"&pn=1&ps=1&index=1&jsonp=jsonp"

    h={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
        "Cookie":"None"
    }

    r_fans=requests.get(url_fans,headers=h).json()
    r_power=requests.get(url_power,headers=h).json()
    r_info=requests.get(url_info,headers=h).json()
    r_video=requests.get(url_video,headers=h).json()
    upname=r_info['data']['name']

    print("以下为UP主信息...")
    print("你查询的UP主[%s]目前的粉丝数为%s个,性别:[%s]"%(upname,r_fans['data']['follower'],r_info['data']['sex']))
    if r_power['code']==0:
        print("是否开通充电: 是")
    else:
        print("是否开通充电: 否")
    print("简介: %s"%r_info['data']['sign'])
    print("会员状态: %s"%r_info['data']['vip']['label']['text'])
    print("使用的头像挂件是(为空的话代表没有使用): %s"%r_info['data']['pendant']['name'])
    print("直播间链接[%s]，标题[%s]"%(r_info['data']['live_room']['url'],r_info['data']['live_room']['title']))
    print("[%s]目前最新一期视频是:[%s]，av号[%s]，BV号[%s]"%(upname,r_video['data']['list']['vlist'][0]['title'],r_video['data']['list']['vlist'][0]['aid'],r_video['data']['list']['vlist'][0]['bvid']))
    print("Bilibili认证: %s"%r_info['data']['official']['title'])
    
    time.sleep(30)
    exit()
