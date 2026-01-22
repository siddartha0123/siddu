import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1/comments"

# 

# 'https://fakestoreapi.com/products'

response = requests.get(API_URL)

if response.status_code == 200:
     data = response.json()
     for i  in data:
          print(i)
else:
     print("Something went wrong")