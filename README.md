# 🚗 Automotive Sales Analytics - Gestão de Performance e Estoque

Este repositório apresenta uma solução completa de Business Intelligence para o setor automotivo. O projeto foca no acompanhamento do ciclo de vida da venda, desde a entrada do veículo em estoque até a análise de lucratividade final por modelo e região.

## 🏗️ Estrutura da Solução
A arquitetura foi desenhada para suportar uma visão 360º da operação, utilizando um modelo dimensional:

- **Tabela Fato (Vendas):** Centraliza as transações com métricas de `ValorVenda`, `Custo` e `Lucro`.
- **Dimensão Veículos:** Atributos detalhados como Marca, Modelo, Ano, Combustível e Status (Vendido, Reservado, Disponível).
- **Dimensão Clientes:** Perfil demográfico incluindo Estado e Idade para análise de público-alvo.

## 🛠️ Tecnologias e Engenharia Aplicada
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
