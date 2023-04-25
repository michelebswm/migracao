from classConn import DatabaseConnection
from dados_insercao_pessoas import lista_pessoas
from dados_insercao_funcionarios import dados_funcionarios
import acesso

db = DatabaseConnection(acesso.server, acesso.port, acesso.database, acesso.username, acesso.password)

# Inserindo valores na tabela situacao
comando = "INSERT INTO situacao (desc_situacao) VALUES ('TRABALHANDO'), ('FALTA'), ('AFASTADO'), ('FERIAS'), " \
          "('DEMITIDO'), ('APOSENTADO'), ('PENSIONISTA');"
db.query(comando)
db.query('SELECT * FROM situacao')
for i in db.cursor.fetchall():
    print(i)

# Inserindo valores na tabela vinculo
comando_vinculo = "INSERT INTO vinculo (desc_vinculo) VALUES %s"
valor_vinculo = ['Estatutario', 'Servidor Publico Efetivo', 'Contrato Prazo Determ. (CLT)', 'Agente Politico',
                 'Celetista', 'Estagiario', 'Servidor Publico nao Efetivo']

tuplas_vinculo = [(valor,) for valor in valor_vinculo]
for valor in tuplas_vinculo:
    db.query(comando_vinculo, (valor,))


db.query('SELECT * FROM vinculo')
for i in db.cursor.fetchall():
    print(i)

# Inserindo valores na tabela cargos
comando_cargo = "INSERT INTO cargos (desc_cargo) VALUES %s"
valores_cargo = ['SECRETÁRIO ESCOLAR', 'SECRETARIO', 'PREFEITO', 'PROFESSOR I', 'PROFESSOR II', 'PROFESSOR III',
                 'PROFESSOR IV']
tuplas_cargos = [(cargo,) for cargo in valores_cargo]
for cargo in tuplas_cargos:
    db.query(comando_cargo, (cargo,))
db.query('SELECT * FROM cargos')
for i in db.cursor.fetchall():
    print(i)

# Inserindo valores na tabela pessoas
comando_pessoas = "INSERT INTO pessoas (nome, cpf, dt_nascimento, email, endereco, numero, bairro, cidade, estado,uf, " \
                  "cep) VALUES %s;"
tuplas_pessoas = [(pessoa, ) for pessoa in lista_pessoas]

for pessoa in tuplas_pessoas:
    db.query(comando_pessoas, pessoa)
db.query('SELECT * FROM pessoas')
for i in db.cursor.fetchall():
    print(i)

# Inserindo valores na tabela funcionarios
comando_funcionarios = 'INSERT INTO funcionarios (i_pessoas, i_situacao, i_vinculo, i_cargo, dt_admissao, salario) ' \
                       'VALUES %s'
tuplas_funcionarios = [(funcionario, ) for funcionario in dados_funcionarios]

for funcionario in tuplas_funcionarios:
    db.query(comando_funcionarios, funcionario)

db.query('SELECT * FROM funcionarios')
for i in db.cursor.fetchall():
    print(i)

db.finalizar_conexao()
