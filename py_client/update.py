import requests

endpoint = "http://127.0.0.1:8000/api/1/update/"

data = {
    'title' : 'peak was here',
    'price' : 20,
}

response = requests.put(endpoint,json=data)
print(response.json())