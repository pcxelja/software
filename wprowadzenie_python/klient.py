#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))
tm = s.recv(1024)
s.close()
print 'Czas serwera: ', tm
