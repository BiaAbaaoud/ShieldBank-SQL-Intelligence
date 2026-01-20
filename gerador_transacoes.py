import pandas as pd
import numpy as np
import random

def criar_dados_bancarios(n_transacoes=1000):
    np.random.seed(42)
    
    # Criando dados normais (compras comuns)
    dados = {
        'ID_Cliente': [random.randint(1000, 1050) for _ in range(n_transacoes)],
        'Valor': np.random.normal(50, 15, n_transacoes).tolist(), # Média de 50 reais
        'Hora': [random.randint(8, 22) for _ in range(n_transacoes)], # Horário comercial
        'Local': [1 for _ in range(n_transacoes)] # Localização habitual (ID 1)
    }
    
    df = pd.DataFrame(dados)
    
    # Inserindo "Fraudes" (Anomalias) manualmente para testar o algoritmo
    fraudes = pd.DataFrame({
        'ID_Cliente': [1025, 1040, 1010],
        'Valor': [4500.00, 2800.00, 9.00], # Valores muito altos ou estranhos
        'Hora': [3, 2, 4], # Madrugada
        'Local': [88, 99, 77] # Localizações estranhas
    })
    
    df = pd.concat([df, fraudes], ignore_index=True)
    df.to_csv('transacoes_bancarias.csv', index=False)
    print("✅ Dataset 'transacoes_bancarias.csv' criado com sucesso!")

if __name__ == "__main__":
    criar_dados_bancarios()