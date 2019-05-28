
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:40:41 2016

@author: zhanghc
"""

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.8.113',8086))

print s.recv(1024)

#for data in ['zhang','liu','wang']:
#    s.send(data)
#    print s.recv(1024)

#s.send('exit')
#s.close()

while True:
	data = raw_input()
	#recv1 =  s.recv(1024)
	#if recv1:
	#	print recv1
	#recv2 =  s.recv(1024)
	#if recv2:
	#	print recv2		
	if data == 'quit':
		break
	s.send(data.encode("utf-8"))
	#recv =  s.recv(1024)
	#print recv
s.send('exit')
s.close()
