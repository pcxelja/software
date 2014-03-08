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
	


zakres = range(1,8)
print zakres
for i in zakres:
	read_input(i)
	print "Port nr: %d " %i
	print "Stan portu: %d" %stan
	write_output(i, stan = 2)
	sleep(1)
	read_input(i)
	print "Port nr: %d " %i
	print "Stan portu po zmianie stanu %d" %stan
	i = i+1
