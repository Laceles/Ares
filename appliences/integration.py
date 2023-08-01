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

attest = pd.DataFrame(data=dados, columns=colunas)
print(attest)

append = conexao.cursor()
for index, row in attest.iterrows:
    append.execute(f"insert into haps values({row})")
