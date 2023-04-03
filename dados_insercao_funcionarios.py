import pandas as pd
from datetime import datetime

funcionarios_df = pd.read_excel('dados_funcionarios.xlsx')

funcionarios_df['dt_admissao'] = funcionarios_df['dt_admissao'].astype(str)

colunas = funcionarios_df.columns.values.tolist()
coluna = [coluna for coluna in colunas]
dados_funcionarios = [tuple(i) for i in funcionarios_df[coluna].values]
