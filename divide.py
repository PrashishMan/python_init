def divide(a, b):
	try:
		result = a/b
	except (ZeroDivisionError, ValueError): 
		print("The value cannot be divided by zero") 
	except TypeError as err:
		print("both a and b must be int or float")
		print(err)

	else:
		print(f" a: {a} divided by b: {b} is {result}")


print(divide(1, "ee"))
print(divide(1, 2))