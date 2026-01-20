import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def detectar_fraudes():
    print("🛡️ ShieldBank-AI: Iniciando análise de transações...")

    # 1. Carregar os dados que geramos no passo anterior
    df = pd.read_csv('transacoes_bancarias.csv')

    # 2. Selecionar características para análise (Features)
    # Não usamos ID_Cliente porque o ID não indica fraude, mas Valor e Hora sim!
    features = ['Valor', 'Hora', 'Local']
    X = df[features]

    # 3. Normalização (Escalonamento)
    # Fundamental para algoritmos de distância e isolamento
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 4. Configurar e Treinar o Isolation Forest
    # contamination=0.01 significa que esperamos que ~1% dos dados sejam anomalias
    modelo = IsolationForest(contamination=0.01, random_state=42)
    df['Previsao'] = modelo.fit_predict(X_scaled)

    # No Isolation Forest: 1 = Normal, -1 = Anomalia (Fraude Suspeita)
    df['Status'] = df['Previsao'].map({1: 'Normal', -1: 'SUSPEITA DE FRAUDE'})

    # 5. Filtrar e Exibir os Resultados
    fraudes_detectadas = df[df['Previsao'] == -1]
    
    print("\n⚠️ RELATÓRIO DE SEGURANÇA - TRANSAÇÕES SUSPEITAS:")
    if not fraudes_detectadas.empty:
        print(fraudes_detectadas[['ID_Cliente', 'Valor', 'Hora', 'Local', 'Status']])
    else:
        print("✅ Nenhuma irregularidade detectada.")

    # Salvar o relatório final
    df.to_csv('relatorio_fraudes.csv', index=False)
    print("\n💾 Relatório completo salvo como 'relatorio_fraudes.csv'")

if __name__ == "__main__":
    detectar_fraudes()