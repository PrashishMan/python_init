class User(object):
	"""docstring for User"""
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age > 0 :
			self._age = age
		else:
			self._age = 0

	# def get_age(self):
	# 	return self._age

	# def set_age(self, age):
	# 	if age > 0:
	# 		self._age = age
	# 	else:
	# 		self._age = 0

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, value):
		self._age = value

	@property
	def full_name(self):
		return f"{self.first}  {self.last}"

	@full_name.setter
	def full_name(self, full_name):
		self.first, self.last = full_name.split(" ")
	

user = User("App", "oop", 12)
print(user.age)
user.age = 20
print(user.age)
print(user.full_name)
user.full_name = "Prashish Man"
print(user.full_name)
print(user.__dict__)