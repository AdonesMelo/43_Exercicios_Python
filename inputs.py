print('#######################################################################################\n')
# 1
# Exemplo de entrada do usuario(Ex: R$ 5.000,00)
faturamento = input('Digite o valor do faturamento: ')

faturamento = faturamento.replace('R$', '').replace('.', '').replace(',', '.') # usando o replace para tratamentos

fat_numerico = float(faturamento) # convertendo texto para numero
perc_imposto = 0.15

imposto = fat_numerico * perc_imposto
print(f'Imposto pago: R${imposto:,.2f}')

print('\n#######################################################################################\n')

# 2
mensagem = 'Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]'

nome = input('Digite o nome completo do colaborado: ').strip()
email = input('Digite o email do colaborado: ').strip().lower()

posicao_espaco = nome.find(' ')
pri_nome = nome[:posicao_espaco].title()

mensagem = mensagem.replace('[Primeiro Nome]', pri_nome).replace('[E-mail padronizado]', email)
print(mensagem)