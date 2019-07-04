import requests
import pdb as pd
url = "https://icanhazdadjoke.com/search"

response = requests.get(url,
	headers = {"Accept" : "application/json"},
     params = {"term" : "cat", "limit" : "5"}
)
data = response.json();
count = len(data['results'])

ind = 1

while count >0:
	results = data['results'][count-1]
	
	print(f"ind: {ind} \t")
	print(results['joke'])
	# for key, value in results.items():	
	# 	if key is not "id":
	# 		print(f" {key} : {value} ")
	ind +=1
	count-=1
