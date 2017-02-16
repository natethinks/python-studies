class Animal:

	def __init__(self):
		self._name = ""
		self._species = ""
		self._gender = ""

	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name

	def set_species(self, species):
		self._species = species

	def get_species(self):
		return self._species

	def set_gender(self, gender):
		self._gender = gender

	def get_gender(self):
		return self._gender

dog = Animal()
dog.set_name("Joe")
dog.set_gender("Male")
dog.set_species("Husky")
print(dog.get_name())
print(dog.get_species())
print(dog.get_gender())
