class Animal(object):
	"""docstring for Animal"""

	def makeSound(self, sound):
		return f"This animal says {sound}"

class Bird(Animal):
	pass

a = Bird()
print(a.makeSound("Twerp"))
print(isinstance(a, Animal))
print(isinstance(a, Bird))


		