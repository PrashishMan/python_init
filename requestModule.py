import requests

URL = "https://www.google.com"
response = requests.get(URL)
print(f"Your request to {URL} reponses : {response.status_code}")
print(request.head)