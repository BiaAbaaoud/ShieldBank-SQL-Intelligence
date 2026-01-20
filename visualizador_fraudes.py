import pandas as pd
import matplotlib.pyplot as plt

def gerar_grafico_premium():
    # Configuração de estilo moderno
    plt.style.use('seaborn-v0_8-muted')
    fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f8f9fa')
    ax.set_facecolor('#ffffff')

    # 1. Carregar dados
    df = pd.read_csv('relatorio_fraudes.csv')
    normais = df[df['Previsao'] == 1]
    fraudes = df[df['Previsao'] == -1]

    # 2. Plotagem com cores vivas
    # Azul Vivo para transações seguras
    ax.scatter(normais['Hora'], normais['Valor'], 
               c='#007bff', label='Transações Seguras', alpha=0.4, s=40, edgecolors='none')

    # Vermelho Neon para as fraudes
    ax.scatter(fraudes['Hora'], fraudes['Valor'], 
               c='#ff4b5c', label='Alertas de Fraude', alpha=0.9, s=150, 
               edgecolors='#930000', linewidth=1.5, marker='o', zorder=5)

    # 3. Design de Eixos e Grid
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(color='#e0e0e0', linestyle='--', linewidth=0.5, alpha=0.7)

    # 4. Legendas e Anotações no Gráfico (O "pulo do gato")
    plt.title('ShieldBank-AI: Monitoramento de Riscos em Tempo Real', 
             fontsize=18, fontweight='bold', color='#2c3e50', loc='left', pad=20)
    
    # Adicionando caixas de texto explicativas diretamente no gráfico
    ax.text(1, 4600, '⚠️ ALTO VALOR / MADRUGADA', fontsize=9, fontweight='bold', 
            color='#930000', bbox=dict(facecolor='#ff4b5c', alpha=0.1, edgecolor='none'))
    
    ax.text(12, 150, '✅ PADRÃO DE CONSUMO SEGURO', fontsize=9, fontweight='bold', 
            color='#0056b3', bbox=dict(facecolor='#007bff', alpha=0.1, edgecolor='none'))

    # 5. Destaque da Zona de Risco (Cinza Moderno)
    ax.axvspan(0, 6, color='#ececec', alpha=0.5, label='Janela Crítica (0h-6h)')

    # Labels e Legenda
    plt.xlabel('Hora da Transação', fontsize=12, color='#555555')
    plt.ylabel('Valor (R$)', fontsize=12, color='#555555')
    
    # Legenda flutuante elegante
    legend = plt.legend(frameon=True, facecolor='white', edgecolor='#e0e0e0', fontsize=10)
    legend.get_frame().set_linewidth(1.0)

    plt.tight_layout()
    print("🚀 Gráfico Premium gerado com sucesso!")
    plt.show()

if __name__ == "__main__":
    gerar_grafico_premium()README.md.txt