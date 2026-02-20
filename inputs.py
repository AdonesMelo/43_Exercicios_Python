print('#######################################################################################\n')
# Exemplo de entrada do usuario(Ex: R$ 5.000,00)
faturamento = input('Digite o valor do faturamento: ')

faturamento = faturamento.replace('R$', '').replace('.', '').replace(',', '.') # usando o replace para tratamentos

fat_numerico = float(faturamento) # convertendo texto para numero
perc_imposto = 0.15

imposto = fat_numerico * perc_imposto
print(f'Imposto pago: R${imposto:,.2f}')

print('\n#######################################################################################\n')