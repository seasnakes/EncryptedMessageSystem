import tkinter
import socket
import threading
import MD5 as MD5
import RC4 as RC4
import RSA as RSA

win=tkinter.Tk()
win.title("客户端1")
win.geometry("300x300+200+20")

ck=None #用来存储客户端的信息

def chaifen(message):   #用于拆分明文与签名
    plain = " "
    signal = " "
    for i in range(0,len(message)):
        if message[i]=='@':
            plain=message[0:i]
            signal=message[i+1:len(message)]

    return plain,signal


def getInfo():  # 接受消息
    while True:
        data = ck.recv(1024)  # 用于接受服务器发送的信息

        key = "569716548"
        box = RC4.init_box(key)
        mingwen = RC4.ex_decrypt(data, box)  # 解密消息

        p = chaifen(mingwen)  # 返回一个包含明文和签名的元组
        print("拆分出的签名：")
        print(p[1])
        s = p[1]
        s = s[2:len(s) - 1]
        s = s.encode(encoding="utf-8")

        m = MD5.md5(p[0])  # 对明文部分使用md5算法生成摘要
        # signal2=KEY.sign(m)
        v = RSA.Verify(m, s)  # 验证签名
        judge(v)  # 判断安全性
        text.insert(tkinter.INSERT, p[0])


def judge(v):
    if v == "SHA-1":
        print("消息未被篡改，且由本人发送。")
    else:
        print("本次通信存在安全隐患！")

def connectServer():
    global ck
    ipStr=eip.get()
    portStr=eport.get()
    userStr=euser.get()
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ipStr,int(portStr)))
    client.send(userStr.encode("utf-8"))
    ck=client

    t=threading.Thread(target=getInfo)
    t.start()

def sendMail():
    friend=efriend.get()#发给谁
    sendStr=esend.get()#发送的消息

    #用MD5生成消息摘要
    abstract=MD5.md5(sendStr)

    #用RSA算法对消息摘要进行签名
    signal1=RSA.sign(str(abstract))

    #生成消息
    message=sendStr+'@'+str(signal1)

    #用RC4算法对消息进行加密
    key="569716548"
    box = RC4.init_box(key)
    cipher=RC4.ex_encrypt(message, box)

    #发送消息
    sendStr=friend+":"+cipher
    ck.send(sendStr.encode("utf-8"))

#tkinter界面配置
labelUse = tkinter.Label(win, text="userName").grid(row=0, column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

labelIp = tkinter.Label(win, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
eport = tkinter.Variable()

entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="启动", command=connectServer).grid(row=3, column=0)
text = tkinter.Text(win, height=5, width=25)
labeltext= tkinter.Label(win, text="显示消息").grid(row=4, column=0)
text.grid(row=4, column=1)

esend = tkinter.Variable()
labelesend = tkinter.Label(win, text="发送的消息").grid(row=5, column=0)
entrySend = tkinter.Entry(win, textvariable=esend).grid(row=5, column=1)

efriend = tkinter.Variable()
labelefriend= tkinter.Label(win, text="发给谁").grid(row=6, column=0)
entryFriend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=1)

button2 = tkinter.Button(win, text="发送", command=sendMail).grid(row=7, column=0)
win.mainloop()

