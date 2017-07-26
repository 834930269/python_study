import socket,threading,time

#IPV4,UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')

def udplink(data,addr):
    s.sendto(b'Hello, %s!' % data,addr)

while True:
    #接收数据
    #recvfrom()方法返回数据和客户端的地址与端口
    data,addr=s.recvfrom(1024)
    t=threading.Thread(target=udplink,args=(data,addr))
    time.sleep(1)
    t.start()
    
