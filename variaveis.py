# 1
Faturamento_inicial = 50000
Percentual_bonus = 0.1

bonus_total = Faturamento_inicial * Percentual_bonus
faturamento_liquido = Faturamento_inicial - bonus_total
print('\n#######################################################################################\n')


print(f'Bonus_total: R${bonus_total:,.2f} | Faturamento líquido: R${faturamento_liquido:,.2f}')

print('\n#######################################################################################\n')

# 2
estoque = 250
vendidos = 78
reposicao = 100

estoque = estoque - vendidos + reposicao
print(f'Estoque atualizado: {estoque} Un.')

print('\n#######################################################################################\n')

# 3
caixas = 1250
caminhao_suporta = 12

total_caminhao_completo = caixas // caminhao_suporta
print(f'Caminhões completos: {total_caminhao_completo} ')

caixas_restantes = caixas % caminhao_suporta
print(f'Caixas restantes: {caixas_restantes}')

print('\n#######################################################################################\n')

# 4
faturamento = 15000
custos = 5000
perc_imposto = 0.15

imposto = faturamento * perc_imposto
lucro_liquido = faturamento - custos - imposto
margem_lucro =  lucro_liquido / faturamento

print(f'Imposto: R${imposto:,.2f}')
print(f'Lucro Líquido: R${lucro_liquido:,.2f}')
print(f'Margem de lucro: {margem_lucro:.2%}')

meta_atigida = margem_lucro > 0.3
print(f'Meta atingida? {meta_atigida}')
if meta_atigida == True:
    print('A meta foi atingida!')
else:
    print('A meta não foi atingida!')

print('\n#######################################################################################\n')

# 5
MESES_POR_ANO = 12
duracao_contrato_meses = 40 # Valor dinamico
anos_contrato = duracao_contrato_meses // MESES_POR_ANO
meses_contrato = duracao_contrato_meses % MESES_POR_ANO

if meses_contrato == 0:
    print(f'O contrato tem duração de {anos_contrato} ano(s)')
else:
    print(f'O contrato tem duração de {anos_contrato} ano(s) e {meses_contrato} mês(es).')

print('\n#######################################################################################\n')