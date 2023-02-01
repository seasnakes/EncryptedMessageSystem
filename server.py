import tkinter
import socket,threading


win=tkinter.Tk()#创建主窗口
win.title('服务器')
win.geometry("300x200")
users={}#用户字典

def run(ck,ca):
    userName=ck.recv(1024)  
    users[userName.decode("utf-8")]=ck#解码并存储用户信息 dict 的一个元素 key为username utf8 值为username
    printStr=""+userName.decode("utf-8")+"连接\n" #在显示框中显示是否连接成功
    text.insert(tkinter.INSERT,printStr)

    while True:
        buffer=[]
        rData=ck.recv(1024) #接受客户端发送的消息
        dataStr=rData.decode("utf-8")
        buffer.append(dataStr)
        infolist=dataStr.split(":")
        #要发送信息的客户端向目标客户端发送消息
        #users[infolist[0]].send((userName.decode("utf-8")+": "+infolist[1]).encode("utf"))
        users[infolist[0]].send((infolist[1]).encode("utf"))

def start():
    ipStr=eip.get()#从输入端中获取ip
    portStr=eport.get()

    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ipStr,int(portStr))) #绑定ip和端口号
    server.listen(10)
    printStr="服务器启动成功\n"
    text.insert(tkinter.INSERT,printStr)

    while True:
        ck,ca=server.accept() #接受所连接的客户端的信息
        t=threading.Thread(target=run,args=(ck,ca))#每连接一个客户端就开启一个线程
        t.start()

def startSever():
    s=threading.Thread(target=start)
    s.start()#开启线程

labelIp = tkinter.Label(win, text='ip').grid(row=0, column=0)
labelPort = tkinter.Label(win, text='port').grid(row=1, column=0)
eip = tkinter.Variable() #server ip
eport = tkinter.Variable()#server port
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=startSever).grid(row=8, column=0)
text = tkinter.Text(win, height=5, width=30)
labeltext = tkinter.Label(win, text='连接消息：').grid(row=3, column=1)
text.grid(row=4, column=1)
win.mainloop()
