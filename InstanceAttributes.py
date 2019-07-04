class User:
	
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -=1
		return f"{self.first} has logout from the room"


	def getFullName(self):
		return self.first + ' ' + self.last

	def isChild(self):
		return self.age < 12

a = User("apple", "sing", 2)
wa = User("applesd", "sings", 3)

print(a.logout())
print(User.active_users)

