import pandas as pd
import random
from datetime import datetime, timedelta

# --- CONFIGURAÇÕES INICIAIS ---
n_veiculos = 80
n_clientes = 50
n_vendas = 100 # Vamos simular 100 vendas

# --- 1. GERANDO TABELA DE VEÍCULOS ---
marcas = {
    "Toyota": ["Corolla", "Hilux", "SW4"],
    "Honda": ["Civic", "HR-V", "Fit"],
    "Volkswagen": ["Polo", "T-Cross", "Nivus"],
    "Chevrolet": ["Onix", "Tracker", "S10"],
    "Hyundai": ["HB20", "Creta"]
}

dados_veiculos = []
for i in range(1, n_veiculos + 1):
    marca = random.choice(list(marcas.keys()))
    modelo = random.choice(marcas[marca])
    preco = random.randint(50000, 200000)
    dados_veiculos.append({
        "VeiculoID": i,
        "Marca": marca,
        "Modelo": modelo,
        "Ano": random.randint(2018, 2024),
        "Combustivel": random.choice(["Flex", "Diesel", "Gasolina"]),
        "Preco": preco,
        "Status": random.choice(["Vendido", "Disponível", "Reservado"])
    })
df_veiculos = pd.DataFrame(dados_veiculos)

# --- 2. GERANDO TABELA DE CLIENTES ---
estados = ["SP", "RJ", "MG", "RS", "BA", "PR"]
dados_clientes = []
for i in range(1, n_clientes + 1):
    dados_clientes.append({
        "ClienteID": i,
        "Nome": f"Cliente {i}",
        "Estado": random.choice(estados),
        "Idade": random.randint(18, 75)
    })
df_clientes = pd.DataFrame(dados_clientes)

# --- 3. GERANDO TABELA DE VENDAS ---
dados_vendas = []
data_inicial = datetime(2024, 1, 1)

for i in range(1, n_vendas + 1):
    valor_venda = random.randint(60000, 220000)
    custo = valor_venda * random.uniform(0.7, 0.9) # Custo é 70% a 90% do valor
    lucro = valor_venda - custo
    
    dados_vendas.append({
        "VendaID": i,
        "DataVenda": (data_inicial + timedelta(days=random.randint(0, 200))).strftime('%Y-%m-%d'),
        "VeiculoID": random.randint(1, n_veiculos), # Relaciona com Veículos
        "ClienteID": random.randint(1, n_clientes), # Relaciona com Clientes
        "ValorVenda": round(valor_venda, 2),
        "Custo": round(custo, 2),
        "Lucro": round(lucro, 2)
    })
df_vendas = pd.DataFrame(dados_vendas)

# --- SALVANDO TUDO ---
df_veiculos.to_csv("tabela_veiculos.csv", index=False)
df_clientes.to_csv("tabela_clientes.csv", index=False)
df_vendas.to_csv("tabela_vendas.csv", index=False)

print("Sucesso! As 3 tabelas foram criadas e salvas em arquivos .csv")
print(f"Veículos: {len(df_veiculos)} | Clientes: {len(df_clientes)} | Vendas: {len(df_vendas)}")
