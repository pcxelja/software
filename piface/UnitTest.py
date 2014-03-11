#!/usr/bin/env python

import unittest
from calculator import CurrencyCalculator

class TestCurrencyCalculator(unittest.TestCase):
	def setUp(self):
		self.calculator = CurrencyCalculator()

	def testCurrencyCalculatorHasEuroExchangeRate(self):
		assert self.calculator.euro_exchange_rate != None, "calculator euro_exchange_rate is None"

	def testCurrencyCalculatorHasPoundExchangeRate(self):
		assert self.calculator.pound_exchange_rate != None, "calculator pound_exchange_rate is None"

	def testCurrencyCalculatorSetEuroExchangeRate(self):
		self.calculator.setEuroExchangeRate(4.1)
		assert self.calculator.euro_exchange_rate == 4.1, "calculator euro_exchange_rate did not set correclty"

	def testCurrencyCalculatorSerEuroExchangeRate(self):
		self.calculator.setPoundExchangeRate(4.6)
		assert self.calculator.pound_exchange_rate == 4.6

	def testCurrencyCalculatorPoundsToPLN(self):
		self.calculator.setPoundExchangeRate(4.6)
		assert self.calculator.poundsToPLN(1) == 4.6
		assert self.calculator.poundsToPLN(2) == 9.2

	def testCurrencyCalculatorEuroToPLN(self):
		self.calculator.setEuroExchangeRate(4.1)
		assert self.calculator.eurosToPLN(1) == 4.1
		assert self.calculator.eurosToPLN(2) == 8.2

if __name__ == "__main__":
	unittest.main()
