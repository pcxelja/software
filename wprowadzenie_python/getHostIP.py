#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import socket
import sys

def getHostIP(domain_name):
	ip_addr = socket.gethostbyname(domain_name)
	return ip_addr

if __name__ == '__main__':
	domain = sys.argv[1]
	print 'Adress IP dla domeny %s to %s' % (domain, getHostIP(domain))

