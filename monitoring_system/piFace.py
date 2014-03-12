#!/usr/bin/env python
import piface.pfio as pfio

pfio.init()

class PiFacePort:
	
	def read_input(port):
		#global stan
		stan = pfio.digital_read(port)
		return stan
		
	def write_output(port,stan):
		pfio.digital_write(port,stan)
