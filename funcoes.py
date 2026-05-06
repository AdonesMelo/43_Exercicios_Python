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