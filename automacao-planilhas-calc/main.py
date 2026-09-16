import pandas as pd
from pathlib import Path

def processar_dados_vendas(caminho_arquivo: str) -> pd.DataFrame:
    """Lê, limpa e padroniza um arquivo individual (CSV ou Excel)."""
    extensao = Path(caminho_arquivo).suffix
    
    # 1. Extração
    if extensao == '.csv':
        df = pd.read_csv(caminho_arquivo)
    elif extensao in ['.xls', '.xlsx']:
        df = pd.read_excel(caminho_arquivo)
    else:
        raise ValueError(f"Formato não suportado: {extensao}")

    # 2. Limpeza e Padronização
    df.columns = [col.upper().strip() for col in df.columns] 
    
    colunas_necessarias = {'PRODUTO', 'VALOR', 'DATA'}
    if not colunas_necessarias.issubset(df.columns):
        raise KeyError(f"O arquivo {caminho_arquivo} não possui as colunas necessárias.")

    df = df.dropna(subset=['PRODUTO', 'VALOR']) 
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce') 
    df['VALOR'] = pd.to_numeric(df['VALOR'], errors='coerce').fillna(0) 
    
    return df

def gerar_relatorio_consolidado(lista_arquivos: list, caminho_saida: str):
    """Consolida múltiplos arquivos e gera um relatório formatado em Excel."""
    dataframes = []

    for arquivo in lista_arquivos:
        try:
            df_limpo = processar_dados_vendas(arquivo)
            dataframes.append(df_limpo)
            print(f"Sucesso: {arquivo} processado e limpo.")
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    if not dataframes:
        print("Nenhum dado válido para consolidar.")
        return

    # 3. Transformação
    df_consolidado = pd.concat(dataframes, ignore_index=True)
    
    resumo_vendas = (
        df_consolidado.groupby('PRODUTO')['VALOR']
        .sum()
        .reset_index()
        .sort_values(by='VALOR', ascending=False)
    )

    # 4. Carga
    with pd.ExcelWriter(caminho_saida, engine='openpyxl') as writer:
        resumo_vendas.to_excel(writer, sheet_name='Resumo_Vendas', index=False)
        df_consolidado.to_excel(writer, sheet_name='Dados_Limpos', index=False)
    
    print(f"\nRelatório gerado com sucesso! Arquivo salvo como: {caminho_saida}")

if __name__ == "__main__":
    arquivos_entrada = ['vendas_filial_A.csv', 'vendas_filial_B.xlsx']
    nome_arquivo_final = 'relatorio_final_consolidado.xlsx'
    
    gerar_relatorio_consolidado(arquivos_entrada, nome_arquivo_final)
