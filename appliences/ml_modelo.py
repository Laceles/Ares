from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import psycopg2
import pandas as pd
import numpy as np

# Criando a conexão
conexao = psycopg2.connect(
    database="air_tox",
    host="localhost",
    user="jrodolfo",
    password="Arcanael2309",
    port="5432",
)
# Carregando conjunto de dados do air_tox
query = "SELECT * FROM air_toxicity_test;"
df = pd.read_sql_query(query, conexao)

# Realizar concatenação dos dados
X = df.drop("incidences", axis=1)
y = df["incidendes"]
# Dividir o conjunto de dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

# Criar o modelo de classificação (Linear Regression)
model = LinearRegression()

# Definir o tamanho do lote
batch_size = 100000

# Treinar o modelo em lotes
for i in range(0, len(X_train), batch_size):
    X_batch = X_train[i : i + batch_size]
    y_batch = y_train[i : i + batch_size]
    model.partial_fit(X_batch, y_batch, classes=np.unique(y))

# Avaliar o modelo no conjunto de teste
accuracy = model.score(X_test, y_test)
print("Acurácia do modelo:", accuracy)
