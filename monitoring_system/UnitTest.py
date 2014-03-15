#!/usr/bin/env python

import unittest
from piFace import PiFacePort

class testMonitoringSystem(unittest.TestCase):
	
	def testMonitoringSystemExist(self):
		PiFace = PiFacePort()
		
	def testReadAnInput(self):
		pass

if __name__ == '__main__':
	unittest.main()
