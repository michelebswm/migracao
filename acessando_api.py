import requests
import json

url = 'http://127.0.0.1:5000/api/pessoas/80'

response = requests.get(url)

if response.status_code != 200:
    print("Erro ao acessar a API " + response.text)

print(response.json())
