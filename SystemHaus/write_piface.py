#!/usr/bin/env python

import piface.pfio as pfio
import sys

pfio.init()

'''
def read_input(i):
	global stan
	stan = pfio.digital_read(i)
	return stan
'''

def main(argv):
	port = int(argv[1])
		if port > 9:
			print 'No correct value PORT: %d' %port
	stan = int(argv[2])
		if stan > 2:
			print 'No correct value STAN %d' %stan
	pfio.digital_write(port,stan)

def print_usage():
	print '''
	You need two arguments: PORT and stan
	'''	
'''
zakres = range(1,9)
print zakres
for i in zakres:
	stan = read_input(i)
	print "Port nr: %d stan portu: %d " %(i, stan)
	i = i+1
'''
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
    else:
        if 
        main(sys.argv)
