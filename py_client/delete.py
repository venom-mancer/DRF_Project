import requests

product_id = input("which product you want to delete :")

try:
    product_id = int(product_id)

except:
    product_id = None
    print("{} not valid anymore".format(product_id))

if product_id:
    endpoint = "http://127.0.0.1:8000/api/{}/delete/".format(product_id)
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)

data = {
    'title' : 'peak was here',
    'price' : 20,
}


response = requests.delete(endpoint,json=data)
print(response.json())