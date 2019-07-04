from termcolor import colored

text = colored("Hello world", color = "white", on_color = 'on_magenta', attrs = ["blink"])
print(text)