#!/usr/bin/env python

#-*- coding: utf-8 -*-

def buildConnectionString(params):
	u"""Tworzymy
	lancuch
	 znakow """
	return ":".join(["%s=%s" % (k,v) for k,v in params.items()])

if __name__ == "__main__":
	myParams = {
		"server":"mpilgrim", \
		"database":"master", \
		"uid":"sa", \
		"pwd":"secret"
		}
	print buildConnectionString(myParams)
