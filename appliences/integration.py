import psycopg2
import pandas as pd
import plotly.express as px
import numpy as np

conexao = psycopg2.connect(
    database="air_tox",
    host="localhost",
    user="jrodolfo",
    password="Arcanael2309",
    port="5432",
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
