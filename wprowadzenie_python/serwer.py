#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while 1:
	client,addr = s.accept()
	print 'Polaczenie' , addr
	client.send(time.ctime(time.time()))
	client.close
