from inheritance import b
class Pet:
	allowed = ["cat", "dog", "fish", "gecko"]

	@classmethod
	def class_attribute(cls):
		print(cls.allowed)

	def __init__(self, name, species):
		if species.lower() not in Pet.allowed:
			raise ValueError(f"You cannot have a {species} pet")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species.lower() not in Pet.allowed:
			raise ValueError(f"You cannot have a {species} pet")
		self.species = species


cat = Pet("vla", "cat")
dot = Pet("chinkey", "dog")
Pet.class_attribute()
print(b)
