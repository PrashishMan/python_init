def sum_all(*args):
	
	if "add" in args:
		add = 0
		for num in args[1:]:
			add += num

		return add
	
	elif "mul" in args:
		mul = 1
		for num in args[1:]:
			mul *= num
		return mul
	return args

print(sum_all("mul", 2, 3, 4, 5, 6))
print(sum_all("add", 2, 3, 4, 5, 6))
