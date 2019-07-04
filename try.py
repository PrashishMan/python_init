try:
	foobar
except NameError:
	print("Problem: ")

d = {"name" : "Prashish", "age" : "24", "gender" : "male"}

def get(d, key):
	try:
		return d[key]
	except KeyError:
		print("key not available")
		return None

print(get(d, "ap"))


while True: 
	try:
		num = int(input("Please enter a number: "))
	except ValueError:
		print("This is not a number")
	else:
		print("Nice, it is a number")
		break
	finally: 
		print("runs no matter what")

print("now you can watch")