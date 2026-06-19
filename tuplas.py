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

print('\n#######################################################################################\n')
# 4
dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

# função que recebe uma tupla e retorna o total de vendas e a média de vendas
def analisar_vendas(lista_vendas):
    total_vendas = sum(lista_vendas)
    media_vendas = total_vendas / len(lista_vendas)

    return total_vendas, media_vendas

# Iterando sobre a lista de filiais
for filial in dados_filiais:
    total_vendas, media_vendas = analisar_vendas(dados_filiais[filial])
    print(f'Filial {filial} -> Total: R${total_vendas:.2f}, Média: R${media_vendas:.2f}')

print('\n#######################################################################################\n')
# 5
tempos = [15, 45, 10, 120, 30] 

def resumo_chamados(lista_chamados):
    quantidade_chamados = len(lista_chamados)
    tempo_maximo_espera = max(lista_chamados)

    return quantidade_chamados, tempo_maximo_espera

qtd, max_espera = resumo_chamados(tempos)
print(f'Foram abertos {qtd} chamados, o tempo máximo de SLA: {max_espera} minutos')

print('\n#######################################################################################\n')