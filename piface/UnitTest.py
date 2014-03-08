import unittest
from calculator import CurrencyCalculator

class TestCurrencyCalculator(unittest.TestCase):
	def testCurrencyCalculatorExist(self):
		calculator = CurrencyCalculator()

	def testCurrencyCalculatorHasEuroExchangeRate(self):
		calculator = CurrencyCalculator()
		assert calculator.euro_exchange_rate != None, "calculator euro_exchange_rate is None"

	def testCurrencyCalculatorHasPoundExchangeRate(self):
		calculator = CurrencyCalculator()
		assert calculator.pound_exchange_rate != None, "calculator pound_exchange_rate is None"

	def testCurrencyCalculatorSetEuroExchangeRate(self):
		calculator = CurrencyCalculator()
		calculator.setEuroExchangeRate(4.1)
		assert calculator.euro_exchange_rate == 4.1, "calculator euro_exchange_rate did not set correclty"

if __name__ == "__main__":
	unittest.main()
