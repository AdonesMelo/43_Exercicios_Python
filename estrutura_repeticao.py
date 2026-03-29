print('\n#######################################################################################\n')

# 1
for i in range(10):
    tempo_regressivo = 10 - i
    print(f'Lembrete: O treinamento de Python começa em {tempo_regressivo} minutos.')

print('\n#######################################################################################\n')

# 2
vendas = [2000, 5000, 1000, 8000, 3000]

comissao_total = 0 
for venda in vendas:
    if venda > 4000:
        comissao = 0.1
    else:
        comissao = 0.05
    
    comissao_total = comissao_total + comissao * venda

print(f'O vendedor receberá R${comissao_total:,.2f}')

print('\n#######################################################################################\n')