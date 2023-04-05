from classConn import DatabaseConnection
from flask import Flask
import simplejson as json


# Inicialização
app = Flask(__name__)

app.json_provider_class = json.JSONEncoder(sort_keys=False)     # Desabilitando ordenação automática

# Define a rota para o método GET
@app.route('/api/situacao', methods=['GET'])
def get_situacao():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM situacao"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result)

@app.route('/api/vinculo', methods=['GET'])
def get_vinculo():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM vinculo"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result)

@app.route('/api/cargos', methods=['GET'])
def get_cargos():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM cargos"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result)

@app.route('/api/pessoas', methods=['GET'])
def get_pessoas():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM pessoas"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'nome': dados[1], 'cpf': dados[2], 'dataNascimento': dados[3], 'email': dados[4],
                'endereco': dados[5], 'numero': dados[6], 'bairro': dados[7], 'cidade': dados[8], 'estado': dados[9],
                'uf': dados[10], 'cep': dados[11]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result)


get_pessoas()
#app.run()
