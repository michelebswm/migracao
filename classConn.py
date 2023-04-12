import pyodbc

class DatabaseConnection:
    """
    Cria uma conexão com banco de dados MySQL ODBC 8.0 Unicode Driver

    Atributos:
        server (str): Nome do servidor, exemplo localhost
        database (str): Nome do banco de dados
        username (str): Usuário de acesso ao servidor
        password (str): Possui um valor padrão '' que pode ser alterado com a senha de acesso ao servidor
    """
    def __init__(self, server, database, username, password=''):
        self.cursor = None
        self.conn = None
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conectar()

    def conectar(self):
        dados_conn = f'DRIVER={{MySQL ODBC 8.0 Unicode Driver}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};encoding=UTF-8'
        self.conn = pyodbc.connect(dados_conn)
        self.cursor = self.conn.cursor()
        print('Conexão realizada com Sucesso')

    def query(self, comando, valores=None):
        if valores:
            try:
                print(self.cursor.execute(comando, valores))
                self.cursor.execute(comando, valores)
                #self.cursor.executemany(comando, [(valor,) for valor in valores])
                self.conn.commit()
            except pyodbc.IntegrityError as e:
                print(f'Ocorreu um erro de Integridade: {e}')
                self.conn.rollback()    # O método rollback() é chamado para desfazer quaisquer alterações feitas no banco de dados se ocorrer um erro.
        else:
            try:
                self.cursor.execute(comando)
                self.conn.commit()
            except pyodbc.IntegrityError as e:
                print(f'Ocorreu um erro de Integridade: {e}')
                self.conn.rollback()

    def verifica_existencia_tabela(self, tabela):
        comando = 'SHOW TABLES LIKE "{}"'.format(tabela)
        self.cursor.execute(comando)
        resultado = len(self.cursor.fetchall())
        if resultado > 0:
            return True
        else:
            return False

    def criando_tabela(self, tabela, campos):
        resultado = self.verifica_existencia_tabela(tabela)
        if resultado is True:
            print('Tabela já existe no banco de dados')
        else:
            comando = 'CREATE TABLE IF NOT EXISTS {}({});'.format(tabela, campos)
            print(comando)
            self.cursor.execute(comando)
            self.conn.commit()

    def finalizar_conexao(self):
        self.cursor.close()
        self.conn.close()
        print('Conexao Finalizada com sucesso')


