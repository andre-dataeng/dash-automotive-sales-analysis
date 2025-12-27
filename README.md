# 🚗 Automotive Sales Analytics - Gestão de Performance e Estoque

Este repositório apresenta uma solução completa de Business Intelligence para o setor automotivo. O projeto foca no acompanhamento do ciclo de vida da venda, desde a entrada do veículo em estoque até a análise de lucratividade final por modelo e região.

## 🏗️ Estrutura da Solução
A arquitetura foi desenhada para suportar uma visão 360º da operação, utilizando um modelo dimensional:

- **Tabela Fato (Vendas):** Centraliza as transações com métricas de `ValorVenda`, `Custo` e `Lucro`.
- **Dimensão Veículos:** Atributos detalhados como Marca, Modelo, Ano, Combustível e Status (Vendido, Reservado, Disponível).
- **Dimensão Clientes:** Perfil demográfico incluindo Estado e Idade para análise de público-alvo.

## ⚙️ Arquitetura de Processamento (Data Pipeline)

Neste projeto, optei por uma estrutura de camadas para garantir a integridade dos dados e a performance do dashboard:

### 🐍 Camada de Saneamento (Python)
O script `etl_automotive.py` não realiza cálculos financeiros; sua função é garantir a **Qualidade de Dados (Data Quality)** antes da carga:
- **Normalização de Strings:** Padronização de Marcas e Modelos para evitar duplicidade por erro de digitação (ex: "honda" vs "Honda").
- **Padronização Geográfica:** Conversão de estados para CAIXA ALTA, garantindo que a geolocalização do Power BI reconheça 100% dos dados no mapa.
- **Deduplicação:** Remoção de registros duplicados que poderiam inflar o volume de vendas.

### 📊 Camada de Inteligência (Power BI & DAX)
Toda a lógica de negócio e cálculos matemáticos foram centralizados diretamente no Power BI através de **DAX (Data Analysis Expressions)**, permitindo que as métricas sejam dinâmicas:
- **Medidas Calculadas:** Ticket Médio, Margem % e Lucro Total.
- **Flexibilidade:** Os cálculos reagem instantaneamente aos filtros de Marca, Ano ou Status do Veículo.
- **Power BI:** Modelagem de dados e criação de dashboards dinâmicos.
- **DAX Avançado:** Desenvolvimento de medidas inteligentes para suporte à decisão:
  - `Ticket Médio`: Valor médio das transações por período.
  - `Margem %`: Eficiência de lucro sobre o faturamento.
  - `Qtd Vendida`: Volume de movimentação de estoque.
- **Processamento de Dados:** Lógica de negócio aplicada para categorização automática de status de veículos e cálculo de lucro direto na fonte de dados.

## 📊 Insights de Negócio
O dashboard permite responder perguntas críticas como:
1. Qual a marca/modelo com maior margem de contribuição?
2. Como está a distribuição de vendas por estado (SP, RJ, MG, BA, RS)?
3. Qual o perfil de idade dos clientes que mais consomem modelos específicos?
4. Qual o percentual de veículos em status 'Disponível' vs 'Reservado' para gestão de pátio?

## 📸 Preview
![Preview do Dashboard](Img%20dash.png)

---
*Desenvolvido por André - Engenheiro de Dados*
