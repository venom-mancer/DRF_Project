import requests

endpoint = "http://127.0.0.1:8000/api/create/"

data = {
    'title' : 'this field is done',
    'price' : 45,
}

response = requests.post(endpoint,json=data)
print(response.json())