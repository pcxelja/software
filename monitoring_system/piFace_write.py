#!/usr/bin/env python
import piface.pfio as pfio
import sys
import time

pfio.init()

#port = int(sys.argv[1])
#stan = int(sys.argv[2])

port = 1
stan = 1


def read_input(port):
	#global stan
	stan = pfio.digital_read(port)
	return stan
		
def write_output(port, stan):
	pfio.digital_write(port, stan)

write_output(port, stan)

time.sleep(10)
write_output(port, 0)
