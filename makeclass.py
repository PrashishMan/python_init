class Adder:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		self.sum = num1 + num2

a1 = Adder(2,3)
a2 = Adder(5,55)
a3 = Adder(100,30)

print(a1.sum)
print(a2.sum)
print(a3.sum)
