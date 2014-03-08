from time import sleep
import piface.pfio as pfio
pfio.init()
while(True):
	pfio.digital_write(0,1) #turn on
	sleep(1)
	pfio.digital_write(0,0) #turn off
	sleep(1)


