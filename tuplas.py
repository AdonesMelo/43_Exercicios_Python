print('\n#######################################################################################\n')

# 1
coordenadas = (-23.5505, -46.6333) # tupla é imutável, ou seja, não pode ser alterada depois de criada

latitude, longitude = coordenadas # desempacotamento de tupla

print(f'Latitude: {latitude}, Longitude: {longitude}')

print('\n#######################################################################################\n')
# 2
def calcular_folha(salario):
    pec_desconto = 0.1
    desconto = salario * pec_desconto
    salario_liquido = salario - desconto
    return salario_liquido, desconto

salario = 5000
salario_liquido, desconto = calcular_folha(salario)
print(f"Desconto: R${desconto:.2f} | Salário Líquido: R${salario_liquido:.2f}")

print('\n#######################################################################################\n')
# 3
#(produto, preco_unitario, quantidade)
vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

# Iterando sobre a lista de vendas
for produto, preco_unitario, quantidade in vendas_dia: # desempacotamento de tupla
    print(f'Produto: {produto:<10} | Total: R${preco_unitario * quantidade:.2f}')