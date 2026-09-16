import pandas as pd
import numpy as np

# Gera um CSV bagunçado
df_csv = pd.DataFrame({
    ' Produto ': ['Teclado', 'Mouse', np.nan, 'Monitor', 'Teclado'],
    'Valor ': ['150.50', '80.00', '120.00', 'erro', '150.50'],
    ' Data': ['2026-09-01', '2026-09-01', '2026-09-02', '2026-09-02', '2026-09-03']
})
df_csv.to_csv('vendas_filial_A.csv', index=False)

# Gera um Excel bagunçado
df_excel = pd.DataFrame({
    'PRODUTO': ['Mouse', 'Headset', 'Monitor', np.nan],
    'VALOR': [80.0, 200.0, 850.0, 100.0],
    'DATA': ['04/09/2026', '04/09/2026', '05/09/2026', '06/09/2026']
})
df_excel.to_excel('vendas_filial_B.xlsx', index=False)

print("Arquivos de teste criados com sucesso!")
