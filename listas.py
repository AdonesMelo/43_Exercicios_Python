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

# 2
estoque = ["monitor", "teclado", "mouse", "headset"]
print(estoque)

estoque.append('webcam')
print('Item adcionado no estoque.')

posicao_teclado = estoque.index('teclado')
estoque[posicao_teclado] = 'teclado mecanico'
print('Item do estoque renomeado.')

impressora_no_estoque = 'impressora' in estoque
print(f'Tem impressora no estoque: {impressora_no_estoque}')

estoque.remove('mouse')
print('Item removido do estoque.')

estoque_atualizado = ', '.join(estoque)
print(f'Estoque atualizado: {estoque_atualizado}')

print('\n#######################################################################################\n')

# 3
fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
print('Ordenando do maior para o menpor')
print(fretes)

top_fretes = fretes[:2]
print('\n2 maiores fretes')
print(top_fretes)


print('\n#######################################################################################\n')