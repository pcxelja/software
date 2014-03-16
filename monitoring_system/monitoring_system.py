#!/usr/bin/env python

import piface.pfio as pfio
from time import sleep
import os

pfio.init()

def read_input(i):
	global stan
	stan = pfio.digital_read(i)
	return stan

def write_output(i,stan):
	pfio.digital_write(i,stan)
	
def takePhoto():
	file_time = (str(time.strftime("%Y-%m-%d, %H-%M-%S")))+(".jpg")
	os.system("raspistill -q 70 -o %s") %s
	
	
#raspistill -q 100 -tl <ms> -o nazwa.jpg	
	
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
