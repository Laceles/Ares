import psycopg2
import pandas as pd
import plotly.express as px
import numpy as np
from sqlalchemy import create_engine


conexao = psycopg2.connect(
    database="air_tox",
    host="localhost",
    user="jrodolfo",
    password="Arcanael2309",
    port="5432",
)
engine = create_engine(
    "postgresql://{}:{}@{}/{}".format(
        "jrodolfo", "Arcanael2309", "localhost", "air_tox"
    )
)

print(conexao.info)
print(conexao.status)

cursor = conexao.cursor()
cursor.execute("select * from air_toxicity_test;")
dados = cursor.fetchall()
colunas = []
for col in cursor.description:
    colunas.append(col[0])
print(colunas)

# Consulta SQL para obter os dados
query = "SELECT * FROM air_toxicity_test;"
df = pd.read_sql_query(query, conexao)

attest = pd.DataFrame(data=dados, columns=colunas)
print(attest)

append = conexao.cursor()
for index, row in file1.iterrows():
    try:
        append.execute(
            f"insert into haps values({list(row.values)})".replace("[", "").replace(
                "]", ""
            )
        )
        conexao.commit()
    except:
        # Em caso de erro, desfaz a transação
        conexao.rollback()
        print(f"Erro ao inserir dados: {Exception}")

append.close()
conexao.close()
