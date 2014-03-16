#!/usr/bin/env python

from subprocess import call
import os

def takePhoto(nic):
	#call([raspidtill -q 70 -o foto.jpg])
	pass
	
take = "raspistill -q 70 -o foto.jpg"	
	
if __name__ == '__main__':
	#takePhoto(nic)
	os.system(take)
