import pandas as pd
import openpyxl

vendas_df = pd.read_excel(r'C:\Users\dev\Documents\cientistaDados\Vendas.xlsx')
#print (vendas_df)

lojaSelecionada = 'Loja 01'
filtro = vendas_df.loc[vendas_df['ID Loja'] == lojaSelecionada]
valorTotal = filtro['Valor Final'].sum()
valorFormatado = f"R${valorTotal:,.2f}"
valorFormatado = valorFormatado.replace(',','x').replace('.',',').replace('x','.')
print(f'Faturamento do mês: {valorFormatado}')

quantidadeProdutos = filtro['Quantidade'].sum()
print(f'Quantidade total de produtos é {quantidadeProdutos}')