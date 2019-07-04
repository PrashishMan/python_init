class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name, species):
		self.name = name;
		self.species = species;

	def make_sound(self, make_sound):
		return f"{self.name} says {make_sound}"


class Bird(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species  = "bird")
		self.breed = breed
		self.toy = toy

	def play(self):
		return f"{self.name} plays with {self.toy}"


a = Bird("Toto", "Cocotoo", "ball")
print(a.make_sound("Cocockokok"))
print(a.play())



		
		