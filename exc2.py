for i in range(20):
	if i == 4 or i == 13:
		print(f"{i} is an unlucky number")
	elif i % 2 == 0:
		print(f"{i} is an even number")
	else:
		print(f"{i} is an odd number")