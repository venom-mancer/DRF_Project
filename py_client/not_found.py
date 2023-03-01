import requests

endpoint = "http://127.0.0.1:8000/api/create/1487427"

data = {
    'title' : 'this field is done',
    'price' : 45,
}

response = requests.get(endpoint,json=data)
print(response.json())