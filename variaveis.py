# 1
Faturamento_inicial = 50000
Percentual_bonus = 0.1

bonus_total = Faturamento_inicial * Percentual_bonus
faturamento_liquido = Faturamento_inicial - bonus_total

print(f'\nBonus_total: R${bonus_total:,.2f} | Faturamento líquido: R${faturamento_liquido:,.2f}\n')

print('#######################################################################################')

# 2
estoque = 250
vendidos = 78
reposicao = 100

estoque = estoque - vendidos + reposicao
print(f'\nEstoque atualizado: {estoque} Un.\n')

print('#######################################################################################')

# 3
caixas = 1250
caminhao_suporta = 12

total_caminhao_completo = caixas // caminhao_suporta
print(f'\nCaminhões completos: {total_caminhao_completo} ')

caixas_restantes = caixas % caminhao_suporta
print(f'Caixas restantes: {caixas_restantes}\n')

print('#######################################################################################')
