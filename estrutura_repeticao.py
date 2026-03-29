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

# 3
estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

for i, quantidade in enumerate(estoque_quantidades):
    if quantidade < 8:
        produto = estoque_produtos[i]
        print(f'ALERTA: O produto {produto} está com apenas {quantidade} unidades no estoque!')

print('\n#######################################################################################\n')