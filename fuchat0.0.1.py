import random
from socket import *

print("欢迎来到Fuchat聊天")
print("这是一个极其简化的聊天室，全程只需按键盘即可")
print("如需要设置一些东西请输入命令，格式“/+<命令名>”")
a = input("输入您的ID名，输入完成后请按enter：")
print(a,"，欢迎您！")
c = input("请问您要建房间，还是加入房间，建立请输入指令“/create”，加入请输入指令“/join”：")
if c == '/create':
    room = random.randint(1,10000000)
    print("创建成功，不过很抱歉，目前用户只能用随机房间号，您的房间号为：",room)
    e = input("是否加如您的房间，是请输入指令”/joinmine“，加入其他房间请输入”/join“：")
    if e == '/joinmine':
        print("加入成功，欢迎来到此房间，此房间为私人房间，退出请输入指令“/exit”")
        IP = '192.168.2.37'
        SERVER_PORT = 50000
        BUFLEN = 1024

        # 实例化一个socket对象，指明协议
        dataSocket = socket(AF_INET, SOCK_STREAM)

        # 连接服务端socket
        dataSocket.connect((IP, SERVER_PORT))

        while True:
            # 从终端读入用户输入的字符串
            toSend = input(a + ":")
            if toSend == '/exit':
                break
            # 发送消息，也要编码为 bytes
            dataSocket.send(toSend.encode())

            # 等待接收服务端的消息
            recved = dataSocket.recv(BUFLEN)
            # 如果返回空bytes，表示对方关闭了连接
            if not recved:
                break
            # 打印读取的信息
            print(recved.decode())

        dataSocket.close()
if c == '/join':
    b = int(input("输入您要找的房间号，只用数字，主房间号为1，输入完成后请按enter："))
    if b == 1:
        print("加入成功，欢迎来到主房间，退出请输入指令“/exit”")
        IP = '192.168.2.37'
        SERVER_PORT = 50000
        BUFLEN = 1024

        # 实例化一个socket对象，指明协议
        dataSocket = socket(AF_INET, SOCK_STREAM)

        # 连接服务端socket
        dataSocket.connect((IP, SERVER_PORT))

        while True:
            # 从终端读入用户输入的字符串
            toSend = input(a + ":")
            if toSend == '/exit':
                break
            # 发送消息，也要编码为 bytes
            dataSocket.send(toSend.encode())

            # 等待接收服务端的消息
            recved = dataSocket.recv(BUFLEN)
            # 如果返回空bytes，表示对方关闭了连接
            if not recved:
                break
            # 打印读取的信息
            print(recved.decode())

        dataSocket.close()