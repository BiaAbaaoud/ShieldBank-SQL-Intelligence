# 🛡️ ShieldBank-SQL-Intelligence

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Linguagem](https://img.shields.io/badge/Python-3.x-blue)
![Database](https://img.shields.io/badge/SQL-SQLite-lightgrey)

## 📌 O que é?
O **ShieldBank-SQL-Intelligence** é um ecossistema de análise de crédito focado em segurança financeira. Ele simula o backend de um banco digital, integrando a robustez de um banco de dados relacional (SQL) com a capacidade analítica da Inteligência Artificial (Machine Learning) para detectar anomalias comportamentais.

## 🎯 Objetivo do Projeto
O objetivo principal é demonstrar como o **SQL** atua como a "espinha dorsal" para projetos de IA. O sistema identifica perfis de risco não apenas por valores estáticos, mas cruzando dados complexos de renda versus histórico de gastos, filtrando o que é um comportamento padrão de quem é um potencial fraudador.

## 🛠️ Ferramentas Utilizadas
* **Python**: Linguagem core para lógica e automação.
* **SQL (SQLite)**: Gerenciamento de dados relacionais e modelagem de tabelas.
* **Pandas**: Manipulação e limpeza de dados extraídos via SQL.
* **Scikit-Learn**: Implementação do algoritmo de IA *Isolation Forest*.
* **Matplotlib & Seaborn**: Geração de dashboards e gráficos de dispersão estatística.

## 📂 Documentação dos Arquivos
Cada documento no repositório representa uma camada da arquitetura do projeto:

1.  **`sistema_credito_sql.py`**: Script de infraestrutura que cria o banco de dados e as tabelas usando comandos DDL (Data Definition Language).
2.  **`shieldbank_credito.db`**: O banco de dados SQLite gerado, contendo as tabelas de Clientes e Histórico de Pagamentos.
3.  **`detectar_fraude.py`**: Primeira versão da IA focada em análise unidimensional (Outliers de Renda).
4.  **`shieldbank_ia_v2.py`**: O "cérebro" do projeto. Realiza **SQL Joins** complexos para unir tabelas e treinar a IA com múltiplas variáveis comportamentais.
5.  **`grafico_fraude.py`**: Ferramenta de visualização que gera o mapa de anomalias com linhas de tendência e identificação de suspeitos.

---

## ❓ FAQ - Perguntas Frequentes

**1. Por que usar SQL em vez de apenas arquivos CSV para a IA?**
O SQL garante a integridade dos dados e permite realizar consultas complexas (Joins) e agregações diretamente na fonte, o que é essencial para escalabilidade em bancos reais.

**2. Qual a função do algoritmo Isolation Forest neste projeto?**
Ele atua isolando observações que são significativamente diferentes da massa de dados. No ShieldBank, ele identifica clientes que possuem uma relação "Renda x Gasto" desproporcional à tendência do grupo.

**3. O que define um cliente como "🚩 ALERTA" no sistema?**
Não é apenas ter renda alta ou baixa, mas sim o distanciamento da linha de tendência esperada. Se o gasto médio foge muito do padrão previsto para aquela faixa de renda, o sistema aciona o alerta.

**4. Como o SQL contribuiu para a precisão da IA 2.0?**
Através de um comando `GROUP BY` e `AVG()`, conseguimos extrair o comportamento histórico de cada cliente. Sem essa agregação via SQL, a IA olharia apenas para dados isolados e não para o comportamento acumulado.

**5. O sistema detecta apenas fraudes de gastos excessivos?**
Não. Ele também detecta "anomalias de subutilização" ou inconsistências cadastrais, como clientes de altíssima renda com gastos quase nulos, o que pode indicar contas inativas ou erros de sistema.

**6. É possível escalar este projeto para milhões de dados?**
Sim. Como a estrutura é baseada em SQL, bastaria trocar o motor SQLite por um PostgreSQL ou SQL Server para suportar volumes massivos de transações mantendo a mesma lógica analítica.

---

**Desenvolvedora:** BiaAbaaoud