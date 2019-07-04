def colorize(text, color):
	colors = ("cyan", "red", "blue", "green", "yellow", "purple")
	if type(text) is not str:
		raise TypeError("text must be an instance string ")

	if type(color) is not str:
		raise TypeError("color must be an instance color ")	

	if color not in colors:
		raise Exception("The color is unidentifird!!")

	print(f"Printed {text} in {color}")

colorize("hello", "green")
colorize("hello", "black")
colorize(44, "green")