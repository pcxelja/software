class CurrencyCalculator:
	def __init__(self):
		self.euro_exchange_rate = 0
		self.pound_exchange_rate = 0

	def setEuroExchangeRate(self, value):
		self.euro_exchange_rate = value

	def setPoundExchangeRate(self, value):
		self.pound_exchange_rate = value

	def eurosToPLN(self, ammount):
		return self.euro_exchange_rate*ammount

	def poundsToPLN(self, ammount):
		return self.pound_exchange_rate*ammount
