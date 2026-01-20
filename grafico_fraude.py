import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Carregar dados
conexao = sqlite3.connect('shieldbank_credito.db')
df = pd.read_sql_query("SELECT * FROM Analise_Comportamental", conexao)
conexao.close()

# 2. Configurar o visual (Dark Theme para destacar as cores)
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))

# 3. Adicionar a Linha de Tendência (O "capricho" visual)
# Ela ajuda a ver a relação normal entre Renda e Gasto
sns.regplot(
    data=df, x='renda_mensal', y='gasto_medio', 
    scatter=False, color='#34495e', line_kws={"ls":"--", "lw":2}, label="Tendência Esperada"
)

# 4. Criar o gráfico de dispersão por cima da linha
grafico = sns.scatterplot(
    data=df, 
    x='renda_mensal', 
    y='gasto_medio', 
    hue='Status_IA', 
    palette={'✅ SEGURO': '#2ecc71', '🚩 ALERTA': '#ff4757'},
    s=120,
    edgecolor='white',
    linewidth=1,
    alpha=0.9
)

# 5. Destacar e Nomear os Alertas
for i in range(df.shape[0]):
    if df.Status_IA[i] == '🚩 ALERTA':
        plt.text(
            df.renda_mensal[i] + 100, 
            df.gasto_medio[i], 
            df.nome[i], 
            fontsize=10, 
            fontweight='bold',
            color='#ff4757',
            bbox=dict(facecolor='black', alpha=0.5, edgecolor='none', pad=1)
        )

# 6. Personalização Profissional
plt.title('🛡️ SHIELDBANK AI: ANÁLISE COMPORTAMENTAL', fontsize=18, fontweight='bold', color='white', pad=20)
plt.xlabel('RENDA MENSAL (R$)', fontsize=12, color='#bdc3c7')
plt.ylabel('GASTO MÉDIO POR FATURA (R$)', fontsize=12, color='#bdc3c7')
plt.legend(title='Veredito da IA', title_fontsize='13', loc='upper left', frameon=True)

# Adicionar uma grade sutil
plt.grid(True, linestyle=':', alpha=0.3)

# 7. Salvar e Mostrar
plt.tight_layout()
plt.savefig('mapa_fraude_premium.png', dpi=300)
print("🎨 Gráfico 'Premium' gerado! Veja o arquivo 'mapa_fraude_premium.png'.")
plt.show()