import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Carregar dados do Banco
conexao = sqlite3.connect('shieldbank_credito.db')
df = pd.read_sql_query("SELECT * FROM Clientes", conexao)

# 2. Rodar a IA
modelo = IsolationForest(contamination=0.1, random_state=42)
df['Previsao'] = modelo.fit_predict(df[['renda_mensal']])
df['Status_Fraude'] = df['Previsao'].apply(lambda x: '🚩 SUSPEITO' if x == -1 else '✅ NORMAL')

# 3. GRAVAR O RESULTADO NO BANCO (A mágica acontece aqui)
# Isso cria uma tabela chamada 'Alertas_IA' com os nomes e o status
df[['nome', 'renda_mensal', 'Status_Fraude']].to_sql('Alertas_IA', conexao, if_exists='replace', index=False)

print("✅ IA processada e resultados gravados na tabela 'Alertas_IA'!")
conexao.close()