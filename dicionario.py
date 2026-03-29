print('\n#######################################################################################\n')

# 1
clientes = {'Lira': 5000, 'Alon': 3000, 'Julia': 4500}

nova_compra = 1500
clientes['Alon'] = clientes['Alon'] + nova_compra

# novo cliente
clientes['Marcos'] = 2000

# lista de clientes atualizada
print(clientes)

print('\n#######################################################################################\n')

# 2
estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input('Digite o nome do produto: ').strip().lower()

if produto in estoque:
    print(f'O produto {produto} tem {estoque[produto]} unidades no estoque.')
else:
    print('Produto não encontrado no sistema')

print('\n#######################################################################################\n')

# 3
vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

# somentes os valores
lista_vendas = list(vendas_regiao.values())
print(lista_vendas)

fat_total = sum(lista_vendas)
print(f'Faturamento total: R$ {fat_total:,.2f}')

media_fat = fat_total / len(lista_vendas)
print(f'Média de faturamento: R$ {media_fat:,.2f}')

print('\n#######################################################################################\n')

# 4
desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
nome = input('Digite o nome do colaborador: ')
print(f'Nome: {nome}')

notas = desempenho[nome]
print(f'Notas: {notas}')
media = sum(notas) / len(notas)
print(f'Media: {media}')

print('\n#######################################################################################\n')

# 5
produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}

remover_item = 'radio'
produtos.pop(remover_item)
print(f'Dicionário atualizado: {produtos}')

conferencia_produto = 'celular'
conferencia_estoque = conferencia_produto in produtos
print(f'O produto está no estoque? {conferencia_estoque}')