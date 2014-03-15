#!/usr/bin/env python

import piface.pfio as pfio
from time import sleep

pfio.init()

def read_input(i):
	global stan
	stan = pfio.digital_read(i)
	return stan

def write_output(i,stan):
	pfio.digital_write(i,stan)
	
zakres = range(1,9)

while(True):
	for i in zakres:
		stan = read_input(i)
		if stan == 1:
			print "!!! Alarm !!!"
			write_output(1,1)
		print "Port nr: %d stan portu: %d " %(i, stan)
		i = i+1
		sleep(0.2)
