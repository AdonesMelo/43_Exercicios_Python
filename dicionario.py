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