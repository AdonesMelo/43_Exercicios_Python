# 1
Faturamento_inicial = 50000
Percentual_bonus = 0.1

bonus_total = Faturamento_inicial * Percentual_bonus
faturamento_liquido = Faturamento_inicial - bonus_total

print(f'Bonus_total: R${bonus_total:,.2f} | Faturamento líquido: R${faturamento_liquido:,.2f}')