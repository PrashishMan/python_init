def persons_color(**kwargs):
	for person, color in kwargs.items() :
		print(f"{color} is {person}'s favorate color")


persons_color(Prashish = "Red", Apple = "Green", Orange = "Yellow")

