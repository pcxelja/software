#!/usr/bin/env python

from time import sleep
import piface.pfio as pfio
pfio.init()
zakres = range(1,9)
while(True):
	for i in zakres:
		pfio.digital_write(i,1) #turn on
		print "Port nr %d stan ON" %i
		sleep(1)
		pfio.digital_write(i,0) #turn off
		sleep(1)
		print "Port nr %d stan OFF" %i
		i = i+1


