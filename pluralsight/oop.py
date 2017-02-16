"""Model for aircraft flights"""

class Flight:

	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("No airline code in '{}'".format(number))

		if not number[:2].isupper():
			raise ValueError("Invalid airline code in '{}'".format(number))

		if not (number[2:].isdigit() and int (number[2:]) <= 9999):
			raise ValueError("Invalide route number '{}'".format(number))

		self._number = number

class Airbus22:
	def __init__(self):
		

class Boeing757:
	def __init__(self):
