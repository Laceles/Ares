import psycopg2
import pandas as pd
import plotly.express as px
import numpy as np

file_HAPS = "database/supplementary_HAPS.csv"
file_LEAD = "database/supplementary_LEAD.csv"
file_NONOxNOy = "database/supplementary_NONOxNOy.csv"
file_VOCS = "database/supplementary_VOCS.csv"

df_HAPS = pd.read_csv(file_HAPS, sep=",")
df_LEAD = pd.read_csv(file_LEAD, sep=",")
df_NONOxNOy = pd.read_csv(file_NONOxNOy, sep=",")
df_VOCS = pd.read_csv(file_VOCS, sep=",")

conexao = psycopg2.connect(
    database="air_tox",
    host="localhost",
    user="postgre",
    password="Arcanael2309",
    port="5432",
)

print(conexao.info)
print(conexao.status)
