# Pipeline de Consolidação e Tratamento de Dados (ETL)

Este projeto consiste em um pipeline de **ETL (Extract, Transform, Load)** desenvolvido em Python com a biblioteca **Pandas**. O objetivo principal é automatizar a leitura, tratamento, validação e consolidação de planilhas de vendas originadas de diferentes fontes (formatos `.csv` e `.xlsx`) que contêm dados ausentes ou inconsistentes, gerando um relatório consolidado em Excel de forma 100% automatizada.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **Pandas**: Leitura, manipulação e agregação de dados.
* **OpenPyxl**: Motor para escrita e formatação de arquivos `.xlsx`.
* **Pathlib**: Manipulação de caminhos de arquivos de forma agnóstica ao sistema operacional.

---

## 📐 Arquitetura da Solução

O fluxo de processamento dos dados segue quatro etapas principais:

| Etapa | Responsabilidade | Comandos Chave |
| :--- | :--- | :--- |
| **1. Extração** | Identificação do formato do arquivo (`.csv` ou `.xlsx`) e carregamento em DataFrames. | `pd.read_csv()`, `pd.read_excel()` |
| **2. Limpeza** | Padronização dos nomes das colunas, remoção de registros nulos e conversão de tipos (datas e valores). | `dropna()`, `to_datetime()`, `to_numeric()` |
| **3. Transformação** | Junção dos dados das diferentes filiais e agrupamento para cálculo do total de vendas por produto. | `pd.concat()`, `groupby()`, `sum()` |
| **4. Carga** | Exportação dos dados consolidados para um arquivo Excel com múltiplas abas (`Resumo_Vendas` e `Dados_Limpos`). | `pd.ExcelWriter()` |

---

## 📁 Estrutura do Projeto

```text
.
├── .venv/                      # Ambiente virtual Python (ignorado pelo git)
├── .gitignore                  # Arquivos desconsiderados no versionamento
├── gerar_dados.py              # Script auxiliar para geração de planilhas de teste (dados sujos)
├── main.py                     # Script principal da automação ETL
└── relatorio_final_consolidado.xlsx # Relatório final gerado automaticamente
