import pandas as pd

def process_automotive_data():
    """
    Simulação de ETL para dados de concessionária.
    Foco: Padronização de estados e cálculo de rentabilidade por veículo.
    """
    # Exemplo de dados brutos
    data = {
        'Modelo': ['Civic', 'Corolla', 'Onix', 'HB20'],
        'Marca': ['Honda', 'Toyota', 'Chevrolet', 'Hyundai'],
        'Valor_Venda': [120000, 130000, 75000, 80000],
        'Custo_Aquisicao': [95000, 105000, 60000, 62000],
        'Estado': ['sp', 'rj', 'mg', 'SP'], # Estados com erro de padrão
        'Status': ['Vendido', 'Vendido', 'Reservado', 'Disponível']
    }
    
    df = pd.DataFrame(data)
    print("--- Iniciando ETL Automotivo ---")

    # 1. Padronização Geográfica (Engenharia de Dados)
    df['Estado'] = df['Estado'].str.upper()

    # 2. Cálculo de KPIs Financeiros
    df['Lucro_Bruto'] = df['Valor_Venda'] - df['Custo_Aquisicao']
    df['Margem_Percentual'] = (df['Lucro_Bruto'] / df['Valor_Venda']) * 100

    # 3. Filtro de Inventário Ativo (Lógica de Negócio)
    estoque_disponivel = df[df['Status'] == 'Disponível']
    
    print(f"Processamento concluído. Veículos em estoque: {len(estoque_disponivel)}")
    print(df[['Modelo', 'Estado', 'Lucro_Bruto', 'Margem_Percentual']])

if __name__ == "__main__":
    process_automotive_data()
