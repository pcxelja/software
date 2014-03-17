#!/usr/bin/env python

from subprocess import call
import os
import time

def takePhoto(nic):
	#call([raspidtill -q 70 -o foto.jpg])
	pass
	
file_time = str((time.strftime("%Y-%m-%d-%H-%M-%S")))+(".jpg")

start = "raspistill -q 70 -w 1024 -h 768 -o " + file_time

os.system(start)
