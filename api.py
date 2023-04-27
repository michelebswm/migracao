from classConn import DatabaseConnection
from flask import Flask, Response, request
import simplejson as json
import acesso


def data_string(campo):
    import datetime
    data_formatada = campo.strftime('%Y-%m-%d')
    return data_formatada


# Inicialização
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB
app.json_provider_class = json.JSONEncoder(sort_keys=False)     # Desabilitando ordenação automática

# MÉTODO GET all tabela situacao
@app.route('/api/situacao', methods=['GET'])
def get_situacao():
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM situacao"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    # O parâmetro content_type define o tipo de conteúdo da resposta. application/json indica que a resposta é uma
    # string JSON. charset=utf-8 define o conjunto de caracteres usado na string JSON.
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET id tabela situacao
@app.route('/api/situacao/<int:id>', methods=['GET'])
def get_situacaoid(id):
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM situacao WHERE i_situacao = %s"
    db.query(comando, (id,))
    result = []
    # O método fetchone é utilizado para obter a primeira linha do resultado da query.
    # Caso não haja resultados, retorna-se um erro 404.
    situacao = db.cursor.fetchone()
    if situacao is None:
        return Response(json.dumps([{'message': 'Situação não encontrada'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 404
    else:
        situ = {'id': situacao[0], 'descricao': situacao[1]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200

# MÉTODO GET all tabela vinculo
@app.route('/api/vinculo', methods=['GET'])
def get_vinculo():
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM vinculo"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET id tabela vinculo
@app.route('/api/vinculo/<int:id>', methods=['GET'])
def get_vinculoid(id):
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM vinculo WHERE i_vinculo = %s"
    db.query(comando, (id,))
    result = []
    # O método fetchone é utilizado para obter a primeira linha do resultado da query.
    # Caso não haja resultados, retorna-se um erro 404.
    vinculo = db.cursor.fetchone()
    if vinculo is None:
        return Response(json.dumps([{'message': 'Vínculo não encontrado'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 404
    else:
        situ = {'id': vinculo[0], 'descricao': vinculo[1]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET all tabela cargos
@app.route('/api/cargos', methods=['GET'])
def get_cargos():
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM cargos"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        situ = {'id': dados[0], 'descricao': dados[1]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET id tabela cargos
@app.route('/api/cargos/<int:id>', methods=['GET'])
def get_cargosid(id):
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM cargos WHERE i_cargo = %s"
    db.query(comando, (id,))
    result = []
    # O método fetchone é utilizado para obter a primeira linha do resultado da query.
    # Caso não haja resultados, retorna-se um erro 404.
    cargo = db.cursor.fetchone()
    if cargo is None:
        return Response(json.dumps([{'message': 'Cargo não encontrado'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 404
    else:
        situ = {'id': cargo[0], 'descricao': cargo[1]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET all tabela pessoas
@app.route('/api/pessoas', methods=['GET'])
def get_pessoas():
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
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
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200
    # Convertendo o dicionário para JSON com ensure_ascii=False não da problema quanto de encoding


# MÉTODO GET id tabela pessoas
@app.route('/api/pessoas/<int:id>', methods=['GET'])
def get_pessoasid(id):
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM pessoas WHERE i_pessoas = %s"
    db.query(comando, (id,))
    result = []
    pessoa = db.cursor.fetchone()
    if pessoa is None:
        return Response(json.dumps([{'message': 'Pessoa não encontrada'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 404
    else:
        nova_data = data_string(pessoa[3])
        situ = {'id': pessoa[0], 'nome': pessoa[1], 'cpf': pessoa[2], 'dataNascimento': nova_data, 'email': pessoa[4],
                'endereco': pessoa[5], 'numero': pessoa[6], 'bairro': pessoa[7], 'cidade': pessoa[8], 'estado': pessoa[9],
                'uf': pessoa[10], 'cep': pessoa[11]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200


# MÉTODO GET all tabela funcionarios
@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM funcionarios"
    db.query(comando)
    result = []
    for dados in db.cursor.fetchall():
        nova_data = data_string(dados[5])
        situ = {'id': dados[0], 'idPessoas': dados[1], 'idSituacao': dados[2], 'idVinculo': dados[3], 'idCargo': dados[4],
                'dataAdmissao': nova_data, 'salario': dados[6]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200
    # Convertendo o dicionário para JSON com ensure_ascii=False não da problema quanto de encoding


# MÉTODO GET id tabela funcionarios
@app.route('/api/funcionarios/<int:id>', methods=['GET'])
def get_funcionariosid(id):
    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)
    comando = "SELECT * FROM funcionarios WHERE i_funcionarios = %s"
    db.query(comando, (id,))
    result = []
    funcionario = db.cursor.fetchone()
    if funcionario is None:
        return Response(json.dumps([{'message': 'Funcionário não encontrado'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 404
    else:
        nova_data = data_string(funcionario[5])
        situ = {'id': funcionario[0], 'idPessoas': funcionario[1], 'idSituacao': funcionario[2],
                'idVinculo': funcionario[3], 'idCargo': funcionario[4],
                'dataAdmissao': nova_data, 'salario': funcionario[6]}
        result.append(situ)
    db.finalizar_conexao()
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json; charset=utf-8'), 200

# METODO POST tabela situacao
@app.route('/api/situacao', methods=['POST'])
def post_situacao():
    file_content = request.json
    if type(file_content) == str:   # Se for uma string transforma em list com o json.loads
        file_content = json.loads(file_content)
    elif type(file_content) == list:
        pass
    else:
        return Response(json.dumps([{'message': 'Formato incorreto'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 400

    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)

    for i in file_content:
        if 'id' in i:
            comando = f'''UPDATE situacao
            SET desc_situacao = CASE
                WHEN EXISTS (SELECT * FROM situacao WHERE i_situacao = {i['id']})
                    THEN %s
                ELSE
                    (SELECT %s FROM situacao LIMIT 1)
                END
            WHERE i_situacao = {i['id']};'''
            db.query(comando, (i['descricao'], i['descricao']))

        else:
            comando = 'INSERT INTO situacao (desc_situacao) VALUES (%s) ON CONFLICT DO NOTHING;'
            db.query(comando, (i['descricao'],))
        return Response(json.dumps([{'message': 'EXECUTADO'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 200

# METODO POST tabela vinculo
@app.route('/api/vinculo', methods=['POST'])
def post_vinculo():
    file_content = request.json
    if type(file_content) == str:   # Se for uma string transforma em list com o json.loads
        file_content = json.loads(file_content)
    elif type(file_content) == list:
        pass
    else:
        return Response(json.dumps([{'message': 'Formato incorreto'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 400

    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)

    for i in file_content:
        if 'id' in i:
            comando = f'''UPDATE vinculo
            SET desc_vinculo = CASE
                WHEN EXISTS (SELECT * FROM situacao WHERE i_vinculo = {i['id']})
                    THEN %s
                ELSE
                    (SELECT %s FROM vinculo LIMIT 1)
                END
            WHERE i_vinculo = {i['id']};'''
            db.query(comando, (i['descricao'], i['descricao']))

        else:
            comando = 'INSERT INTO vinculo (desc_vinculo) VALUES (%s) ON CONFLICT DO NOTHING;'
            db.query(comando, (i['descricao'],))
        return Response(json.dumps([{'message': 'EXECUTADO'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 200

# METODO POST tabela cargos
@app.route('/api/cargos', methods=['POST'])
def post_cargos():
    file_content = request.json
    if type(file_content) == str:   # Se for uma string transforma em list com o json.loads
        file_content = json.loads(file_content)
    elif type(file_content) == list:
        pass
    else:
        return Response(json.dumps([{'message': 'Formato incorreto'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 400

    db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)

    for i in file_content:
        if 'id' in i:
            comando = f'''UPDATE cargos
            SET desc_cargo = CASE
                WHEN EXISTS (SELECT * FROM cargos WHERE i_cargo = {i['id']})
                    THEN %s
                ELSE
                    (SELECT %s FROM cargos LIMIT 1)
                END
            WHERE i_cargo = {i['id']};'''
            db.query(comando, (i['descricao'], i['descricao']))

        else:
            comando = 'INSERT INTO cargos (desc_cargo) VALUES (%s) ON CONFLICT DO NOTHING;'
            db.query(comando, (i['descricao'],))
        return Response(json.dumps([{'message': 'EXECUTADO'}], ensure_ascii=False),
                        content_type='application/json; charset=utf-8'), 200

app.run()

