import psycopg2
from psycopg2.errors import UniqueViolation

class DatabaseConnection:
    """
    Cria uma conexão com banco de dados MySQL ODBC 8.0 Unicode Driver

    Atributos:
        server (str): Nome do servidor, exemplo localhost
        database (str): Nome do banco de dados
        username (str): Usuário de acesso ao servidor
        password (str): Possui um valor padrão '' que pode ser alterado com a senha de acesso ao servidor
    """
    def __init__(self, server, port, database, username, password):
        self.cursor = None
        self.conn = None
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conectar_postgre()

    def conectar_postgre(self):
        dados_conn = f'host={self.server} port={self.port} dbname={self.database} user={self.username} password={self.password} sslmode=prefer connect_timeout=10'
        self.conn = psycopg2.connect(dados_conn)
        self.cursor = self.conn.cursor()
        print('Conexão realizada com Sucesso')

    def query(self, comando, valores=None):
        if valores:
            try:
                #print(self.cursor.execute(comando, valores))
                self.cursor.execute(comando, valores)
                #self.cursor.executemany(comando, [(valor,) for valor in valores])
                self.conn.commit()
            except psycopg2.errors.UniqueViolation as e:
                print(f'Ocorreu um erro de Integridade: {e}')
                self.conn.rollback()    # O método rollback() é chamado para desfazer quaisquer alterações feitas no banco de dados se ocorrer um erro.
        else:
            try:
                self.cursor.execute(comando)
                self.conn.commit()
            except psycopg2.errors.UniqueViolation as e:
                print(f'Ocorreu um erro de Integridade: {e}')
                self.conn.rollback()

    def verifica_existencia_tabela(self, tabela):
        comando = "SELECT EXISTS(SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = '{}')".format(tabela)
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()[0]
        if resultado is False:
            return False
        else:
            return True

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
