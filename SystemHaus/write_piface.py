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
	stan = int(argv[2])
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
        main(sys.argv)
