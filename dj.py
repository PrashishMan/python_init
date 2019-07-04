from pyfiglet import figlet_format as ff
from termcolor import colored as c 
import random as r
import requests

url = "https://icanhazdadjoke.com/search"

print(c(ff("Dad jokes 9999"), color = "magenta"))

search = input("Please enter the search value: ")

response = requests.get(url, 
	headers = {"Accept": "application/json"},
	params  = {"term" : search }
)

result = (response.json())['results']
count = 1

if len(result):
	print(f"I have got {len(result)} related jokes here is one")
	print(r.choice(result)["joke"])

else:
	print(f"sorry we done have joke related to {search} please try again")


# for jk in result:
# 	print(f"Joke {count}:  {jk['joke']}")

# 	count += 1