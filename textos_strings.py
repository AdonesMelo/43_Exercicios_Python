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