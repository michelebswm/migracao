from classConn import DatabaseConnection
from flask import Flask
import simplejson as json


def data_string(campo):
    import datetime
    data_formatada = campo.strftime('%Y-%m-%d')
    return data_formatada

# Inicialização
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB


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
    return json.dumps(result, ensure_ascii=False)

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
    return json.dumps(result, ensure_ascii=False)

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
    return json.dumps(result, ensure_ascii=False)

@app.route('/api/pessoas', methods=['GET'])
def get_pessoas():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM pessoas"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        nova_data = data_string(dados[3])
        situ = {'id': dados[0], 'nome': dados[1], 'cpf': dados[2], 'dataNascimento': nova_data, 'email': dados[4],
                'endereco': dados[5], 'numero': dados[6], 'bairro': dados[7], 'cidade': dados[8], 'estado': dados[9],
                'uf': dados[10], 'cep': dados[11]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result, ensure_ascii=False)
    # Convertendo o dicionário para JSON com ensure_ascii=False não da problema quanto de encoding

@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    db = DatabaseConnection('localhost', 'funcionario', 'root')
    comando = "SELECT * FROM funcionarios"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        nova_data = data_string(dados[5])
        situ = {'id': dados[0], 'idPessoas': dados[1], 'idSituacao': dados[2], 'idVinculo': dados[3], 'idCargo': dados[4],
                'dataAdmissao': nova_data, 'salario': dados[6]}
        result.append(situ)
    db.finalizar_conexao()
    return json.dumps(result, ensure_ascii=False)
    # Convertendo o dicionário para JSON com ensure_ascii=False não da problema quanto de encoding


app.run()
