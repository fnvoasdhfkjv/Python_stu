#-*- coding:utf-8 -*-
#..

import sys , socket

print '����һ���������˲���'
server = ('localhost'  , 50015)

sock =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.bind(server)
sock.listen(5)
conn , address = sock.accept()  
#accept��һ�������ĳ��� ,ֻ�����Ӻ�Ż�ִ���������

print 'connetc by ' , address

while True:
    data = conn.recv(1024)
    if not data:
        break
    print data
    conn.send(data)
#sock.close()
