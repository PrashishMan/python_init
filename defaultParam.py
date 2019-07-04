def add(a, b):
	return a + b

def subtract(a, b):
	return a-b

def opp( a, b, fn = add):
	return fn(a, b)


print(opp(4, 2, subtract)) 
print(opp(4, 3))