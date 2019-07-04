class Apple:
	active_users = 0

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",");
		return cls(first,last, age)

	def __repr__(self):
		return f"{self.first} {self.last}"
	
	def __init__(popo, first, last, address):
		popo.first = first
		popo.last = last
		popo.address = address

	def get_full_name(popo):
		return f"{popo.first} {popo.last}"

	def get_address(self):
		return self.address

	def get_initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"
	
b = Apple("Apple", "Singh", "India")

a = Apple.from_string("Apple,Singh,29")
up = str(a)
print(up)
