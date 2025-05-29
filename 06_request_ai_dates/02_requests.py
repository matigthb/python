# Peticiones a APIs 

# Sin dependencias

import urllib.request
import json

try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"

    response = urllib.request.urlopen(api_posts)
    data = response.read()

    json_data = json.loads(data.decode('utf-8'))

    print(json_data)

    response.close()
except urllib.error.URLError as e:

    print(f"Error en la solicitud: {e}")

# Con dependencias (requests)

import requests

#GET
response = requests.get(api_posts)
json= response.json()
#print(json[0])

#POST
import requests

try:    
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    input={
        "title": "titulo",
        "body": "descripcion",
        "userId": 5
    }

    response = requests.post(api_posts,input)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


#PUT
import requests

try:    
    api_posts = "https://jsonplaceholder.typicode.com/posts/1"
    input={
        "title": "titulo",
        "body": "descripcion",
        "userId": 5
    }

    response = requests.put(api_posts,input)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


