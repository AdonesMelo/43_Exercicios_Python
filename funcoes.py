print('\n#######################################################################################\n')

# 1
produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " caixa de som bluetooth " ]

def padronizar_texto(texto):
    texto = texto.strip().title() # remover os espaços vazio e a primeira letra maiuscula

    return texto

# 3 formas de fazer a lista
# 1 opção
produtos_padronizados = []
for produto in produtos_baguncados:
    produto_padronizado = padronizar_texto(produto)
    produtos_padronizados.append(produto_padronizado)
print('1 opção')
print(produtos_padronizados)

# 2 opção
produtos_padronizados_2 = [padronizar_texto(produto) for produto in produtos_baguncados]
print('2 opção')
print(produtos_padronizados_2)

# 3 opção
produtos_padronizados_3 = list(map(padronizar_texto, produtos_baguncados))
print('3 opção')
print(produtos_padronizados_3)

print('\n#######################################################################################\n')

# 2
def calcular_iss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
    
    imposto = valor * taxa

    return imposto

print(f'Imposto de uma nota de R$ 8.000,00 --> imposto R$ {calcular_iss(8000):,.2f}')

print(f'Imposto de uma nota de R$ 3.000,00 --> imposto R$ {calcular_iss(3000):,.2f}')

print('\n#######################################################################################\n')

# 3
def analisar_margem(faturamento, custo):
    lucro = faturamento - custo
    margem = lucro / faturamento

    if margem >= 0.3:
        return 'Margem Saudável'
    else:
        return 'Margem Baixa'

faturamento = float(input('Digite o faturamento: '))
custo = float(input('Digite o custo: '))

resultado_analise = analisar_margem(faturamento, custo)
print(resultado_analise)

print('\n#######################################################################################\n')

# 4
def quem_bateu_meta(fataramento_vendedores, meta):
    for vendedor in fataramento_vendedores:
        if fataramento_vendedores[vendedor] >= meta:
            print(f'Vendedor {vendedor} bateu a meta!')

equipe_vendas = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200, "Paulo": 5000 }
meta_objetivo = 10000

quem_bateu_meta(equipe_vendas, meta_objetivo)

print('\n#######################################################################################\n')