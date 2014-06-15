#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys

def main():
	
	HOST="pi@192.168.1.13"
	# Ports are handled in ~/.ssh/config since we use OpenSSH
	COMMAND="uname -a"

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
		shell = False,
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE)
	
	result = ssh.stdout.readlines()
	if result == []:
		error = ssh.stderr.readlines()
		print >>sys.stderr, "ERROR: %s" % error
	else:
		print result
	
	return 0

if __name__ == '__main__':
	main()
