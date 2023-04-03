import json
from datetime import datetime
with open('dadosPessoas.json', encoding='utf-8') as pessoas_json:
    dados = json.load(pessoas_json)

lista_pessoas = []
for item in dados:
    nome = item['nome']
    cpf = item['cpf']
    data_nasc = item['data_nasc'].replace('/', '-')
    data_obj = datetime.strptime(data_nasc, '%d-%m-%Y')
    data_nasc_formatada = data_obj.strftime('%Y-%m-%d')
    email = item['email']
    endereco = item['endereco']
    numero = item['numero']
    bairro = item['bairro']
    cidade = item['cidade']
    estado = 'Santa Catarina'
    uf = item['estado']
    cep = item['cep']
    lista_pessoas.append((nome, cpf, data_nasc_formatada, email, endereco, numero, bairro, cidade, estado, uf, cep))

#print(lista_pessoas)

