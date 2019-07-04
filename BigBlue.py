from pyfiglet import figlet_format as ff
from termcolor import colored as co

colors = ("red", "blue", "green", "cyan", "magneta", "white", "yellow")

def print_big(text, color):
	result = ff(value)
	if color in colors:
		coloredText = co(result, color = color)
	else:
		coloredText = co(result, color = "red")
	print(coloredText)


value = input("Please enter a sentence to change: ")
color = input("Please enter a color to change: ").lower()

print_big(value, color)