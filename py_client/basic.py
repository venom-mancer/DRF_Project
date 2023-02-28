import requests

endpoint = "http://127.0.0.1:8000/api/"

response = requests.post(endpoint,json={"title" : 'peak'})
print(response.json())