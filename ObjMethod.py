class Apple:
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
	
a = Apple("Apple", "Singh", "India")

print(a.get_full_name())
print(a.get_address())
print(a.get_initials())
print(a.likes("Apple"))