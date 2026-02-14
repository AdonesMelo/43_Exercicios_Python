# 1
faturamento = 45000
custo = 23500
lucro = faturamento - custo
margem = lucro / faturamento

print('\n#######################################################################################\n')

print(f'Lucro: R${lucro:,.2f} | margem: {margem:.0%}')

print('\n#######################################################################################\n')

# 2
nome = ' mArCoS aNtOnIo rOcHa '
email = ' MARCOS.ROCHA@GMAIL.COM '

nome = nome.strip().title()
print(nome)

email = email.strip().lower()
print(email)

print('\n#######################################################################################\n')

# 3
email = 'beatriz.oliveira@empresa.com'
novo_dominio = '@grupocorp.com'

# posicao_a = email.find('@')
# print(posicao_a)

# email = email[:16] + novo_dominio
# print(email)

email = email.replace('@empresa.com', '@grupocorp.com')
print(email)
print('\n#######################################################################################\n')