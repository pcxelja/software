#!/usr/bin/env python

import unittest
from piFace import PiFacePort

class testMonitoringSystem(unittest.TestCase):
	
	def testMonitoringSystemExist(self):
		PiFace = PiFacePort()

if __name__ == '__main__':
	unittest.main()
