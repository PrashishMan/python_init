import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers = {"Accept" : "application/json"})
data = response.json();
print(type(data))
for key, value in data.items():
	print(f"key : {key} and value : {value} ")
