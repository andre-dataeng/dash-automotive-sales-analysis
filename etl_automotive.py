import pandas as pd

def preparar_dados_concessionaria():
    """
    Foco: Saneamento e Padronização.
    Os cálculos de KPIs (Lucro, Margem, Ticket Médio) 
    são realizados via DAX no Power BI.
    """
    
    # 1. CARGA DE DADOS BRUTOS (Simulando suas planilhas)
    veiculos_raw = {
        'VeiculoID': [1, 2, 4, 16],
        'Marca': ['honda', 'Chevrolet', 'HYUNDAI', 'honda '], # Dados com erros de padronização
        'Modelo': ['Civic', 'Cruze', 'HB20', 'Civic'],
        'Status': ['Vendido', 'Disponível', 'Vendido', 'Disponível']
    }
    
    clientes_raw = {
        'ClientID': [1, 2, 3],
        'Estado': ['sp', 'RJ', 'mg'] # Estados em minúsculo
    }

    df_veiculos = pd.DataFrame(veiculos_raw)
    df_clientes = pd.DataFrame(clientes_raw)

    print("--- Iniciando Saneamento de Dados para Power BI ---")

    # 2. TRANSFORMAÇÃO (Limpeza de strings e Normalização)
    
    # Padronizando Marcas para Maiúsculo e removendo espaços extras
    df_veiculos['Marca'] = df_veiculos['Marca'].str.upper().str.strip()

    # Padronizando Estados para Maiúsculo (Garante que o Mapa no BI funcione 100%)
    df_clientes['Estado'] = df_clientes['Estado'].str.upper()

    # Removendo possíveis duplicatas que podem inflar o Total de Vendas
    df_veiculos = df_veiculos.drop_duplicates()

    print("\n✅ Dados normalizados e prontos para o Power BI.")
    print(df_veiculos[['VeiculoID', 'Marca', 'Status']].head())
    print("\n✅ Estados padronizados:")
    print(df_clientes['Estado'].unique())

    return df_veiculos, df_clientes

if __name__ == "__main__":
    preparar_dados_concessionaria()
