# 1
print('\n#######################################################################################\n')

vendas = [1500, 2000, 800, 3500, 1200]

total_vendas = sum(vendas)
qtd_dias = len(vendas)
media_vendas = total_vendas / qtd_dias
melhor_venda = max(vendas)
pior_venda = min(vendas)

print(f'Total de venda na semana: {total_vendas}')
print(f'Média de vendas diária: {media_vendas}')
print(f'A melhor venda: {melhor_venda} | A pior venda: {pior_venda}')

print('\n#######################################################################################\n')