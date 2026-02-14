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
email = 'andre_silva@empresa.com.br'
novo_dominio = '@grupocorp.com'

posicao_a = email.find('@')
#print(posicao_a)

dominio_antigo = email[posicao_a:]
#print(dominio_antigo)

email_novo = email.replace(dominio_antigo, novo_dominio)
print(email_novo)

print('\n#######################################################################################\n')