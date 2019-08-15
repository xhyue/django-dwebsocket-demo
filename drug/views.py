from django.shortcuts import render
import time
from dwebsocket.decorators import accept_websocket
from collections import defaultdict
from .models import Device

# 保存所有接入的用户地址
allconn = defaultdict(list)

@accept_websocket
def build_socket(request, user_id):
    """初始化时建立websocket连接, 保存所有连接"""
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    #判断是不是websocket连接
    if request.is_websocket():
        # 将链接(请求？)存入全局字典中
        allconn[str(user_id)] = request.websocket
        # for msg in request.websocket:
        #
        #     print(msg.decode('utf-8'))

        # device_status = request.websocket.read()
        # device_status = device_status.decode('utf-8')
        # if device_status == "on":
        #     device_status = 1
        # elif device_status == "off":
        #     device_status = 0
        # device_db = Device.objects.create(device_name="lamp", device_status=device_status)
        # send_status = device_db.device_status
        # 遍历请求地址中的消息
        # for message in allconn:
        #     send_ads = allconn[message]
        #     print("", send_ads)
        for message in request.websocket:
            # 将信息发至自己的聊天框
            # request.websocket.send(message)
            # 将信息发至其他所有用户的聊天框
            for i in allconn:
                print(i)
                if i != user_id:
                    allconn[i].send(message)


def send_socket(request):
    for i in allconn:
        allconn[i].send("hahaha")
    return True








