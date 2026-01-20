import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Conexão e União de Dados (SQL avançado)
conexao = sqlite3.connect('shieldbank_credito.db')
query = '''
SELECT 
    c.nome, 
    c.renda_mensal, 
    AVG(p.valor_fatura) as gasto_medio
FROM Clientes c
JOIN Historico_Pagamentos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente
'''
df = pd.read_sql_query(query, conexao)

# 2. Treinando a IA com DUAS variáveis (Renda e Gasto)
# O modelo agora entende a relação entre ganhar e gastar
modelo = IsolationForest(contamination=0.05, random_state=42)
df['Previsao'] = modelo.fit_predict(df[['renda_mensal', 'gasto_medio']])
df['Status_IA'] = df['Previsao'].apply(lambda x: '🚩 ALERTA' if x == -1 else '✅ SEGURO')

# 3. Salvar o veredito final
df.to_sql('Analise_Comportamental', conexao, if_exists='replace', index=False)

print("🚀 IA 2.0 Finalizada! A análise agora é baseada em Comportamento Financeiro.")
conexao.close()