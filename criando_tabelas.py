from classConn import DatabaseConnection

db = DatabaseConnection('localhost', 'funcionario', 'root')

# Criando Tabelas do Banco de Dados
db.criando_tabela('vinculo', 'i_vinculo SMALLINT AUTO_INCREMENT PRIMARY KEY, desc_vinculo VARCHAR(100) NOT NULL UNIQUE')
db.criando_tabela('cargos', 'i_cargo SMALLINT AUTO_INCREMENT PRIMARY KEY, desc_cargo VARCHAR(100) NOT NULL UNIQUE')
db.criando_tabela('situacao', 'i_situacao SMALLINT AUTO_INCREMENT PRIMARY KEY, desc_situacao VARCHAR(100) NOT NULL UNIQUE')
db.criando_tabela('pessoas', 'i_pessoas SMALLINT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(100), cpf VARCHAR(11), '
                             'dt_nascimento DATE, email VARCHAR(60), endereco VARCHAR(120), numero SMALLINT, bairro '
                             'VARCHAR(30), cidade VARCHAR(35), estado VARCHAR(20), uf CHAR(2), cep CHAR(9)')
db.criando_tabela('funcionarios', 'i_funcionarios SMALLINT AUTO_INCREMENT PRIMARY KEY, i_pessoas SMALLINT NOT NULL, '
                                  'i_situacao SMALLINT NOT NULL, i_vinculo SMALLINT NOT NULL, i_cargo SMALLINT NOT NULL,'
                                  ' dt_admissao DATE NOT NULL, salario DECIMAL NOT NULL, FOREIGN KEY (i_pessoas) REFERENCES'
                                  ' pessoas(i_pessoas), FOREIGN KEY (i_situacao) REFERENCES situacao(i_situacao), FOREIGN KEY'
                                  ' (i_vinculo) REFERENCES vinculo(i_vinculo), FOREIGN KEY (i_cargo) REFERENCES cargos(i_cargo)')
db.finalizar_conexao()






