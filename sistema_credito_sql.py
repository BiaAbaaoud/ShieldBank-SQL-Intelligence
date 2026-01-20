import sqlite3
import pandas as pd
import random

# 1. Conexão
conexao = sqlite3.connect('shieldbank_credito.db')
cursor = conexao.cursor()

# 2. Criando as Tabelas
cursor.execute('CREATE TABLE IF NOT EXISTS Clientes (id_cliente INTEGER PRIMARY KEY, nome TEXT, renda_mensal REAL)')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Historico_Pagamentos (
    id_pagamento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    status_pagamento TEXT,
    valor_fatura REAL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
)''')

# 3. Gerando Dados para 50 Clientes (Fictícios)
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Marcos", "Paula"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Almeida"]

clientes_50 = []
for i in range(101, 151):
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    renda = round(random.uniform(2000, 10000), 2)
    clientes_50.append((i, nome_completo, renda))

pagamentos_50 = []
for c in clientes_50:
    id_cliente = c[0]
    for _ in range(random.randint(3, 5)): 
        status = random.choice(['Em dia', 'Em dia', 'Em dia', 'Atrasado']) 
        valor = round(random.uniform(500, 4000), 2)
        pagamentos_50.append((id_cliente, status, valor))

# Limpando dados antigos
cursor.execute("DELETE FROM Historico_Pagamentos")
cursor.execute("DELETE FROM Clientes")

# Inserindo novos dados
cursor.executemany('INSERT INTO Clientes VALUES (?,?,?)', clientes_50)
cursor.executemany('INSERT INTO Historico_Pagamentos (id_cliente, status_pagamento, valor_fatura) VALUES (?,?,?)', pagamentos_50)
conexao.commit()

# 4. Consulta SQL com JOIN
query = '''
SELECT 
    c.nome, 
    c.renda_mensal,
    COUNT(p.id_pagamento) as total_faturas,
    SUM(case when p.status_pagamento = 'Em dia' then 1 else 0 end) as pagamentos_ok
FROM Clientes c
JOIN Historico_Pagamentos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente
'''

df = pd.read_sql_query(query, conexao)

# 5. Inteligência de Crédito (Cálculos e Regras)
df['Score'] = (df['pagamentos_ok'] / df['total_faturas']) * 100

def avaliar_status(linha):
    if linha['Score'] > 70 and linha['renda_mensal'] > 4000:
        return '✅ APROVADO'
    elif linha['Score'] > 50:
        return '🟡 EM ANÁLISE'
    else:
        return '❌ RECUSADO'

df['Decisao_Final'] = df.apply(avaliar_status, axis=1)

# Ordenando para ver os melhores primeiro
df = df.sort_values(by='Score', ascending=False)

# 6. Resultados no Terminal
print("\n" + "="*65)
print("             SHIELDBANK - RELATÓRIO DE CRÉDITO")
print("="*65)
print(df[['nome', 'Score', 'renda_mensal', 'Decisao_Final']].head(15))
print("...")
print(f"\nTotal analisado: {len(df)} clientes.")
print(f"Média de Saúde Financeira: {df['Score'].mean():.2f}%")
print("="*65)

# Fechar conexão
conexao.close()