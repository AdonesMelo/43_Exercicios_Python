# 1
print('\n#######################################################################################\n')

valor_investimento = input('Digite o valor do investimento: ')
valor_investimento = valor_investimento.replace('R$', '').replace('.', '').replace(',', '.')
valor_investimento = float(valor_investimento)

if valor_investimento < 1000:
    print('Perfil iniciante: Sugerimos Tesouro Direto')
elif valor_investimento <= 5000:
    print('Perfil moderado: Sugerimos Fundos Imobiliários')
else:
    print('Perfil arrojado: Sugerimos Ações')

print('\n#######################################################################################\n')
