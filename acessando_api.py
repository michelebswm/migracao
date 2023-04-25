import requests
import json

# url = 'http://127.0.0.1:5000/api/situacao'
# response = requests.get(url)
#
# if response.status_code != 200:
#     print("Erro ao acessar a API " + response.text)
#
# print(response.json())

data = json.dumps([{"descricao": "TESTE"}])


response = requests.post('http://127.0.0.1:5000/api/situacao', json=data)
print(response.text)
