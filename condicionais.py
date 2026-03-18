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

# 2
admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

email = input('Digite o seu email: ').strip().lower()

if email in admins:
    print('Acesso liberado! Bem-vindo ao painel de controle')
else:
    print('Acesso negado. Você não tem permissões de administrador')

print('\n#######################################################################################\n')

# 3
valor_carrinho = 500

if valor_carrinho < 200:
    perc_desconto = 0
elif valor_carrinho < 500:
    perc_desconto = 0.1
else:
    perc_desconto = 0.15

desconto = valor_carrinho * perc_desconto
valor_final = valor_carrinho - desconto

print(f'O desconto foi de R${desconto:,.2f} e o valor a ser pago é de {valor_final:,.2f}')

print('\n#######################################################################################\n')

# 4
meta_vendedor = 1000
vendas_vendedor = 1000

meta_loja = 5000
vendas_loja = 4000

if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    bonus = 0.2 * vendas_vendedor
else:
    bonus = 0

print(f'Seu bônus este mês é de: R${bonus:,.2f}')