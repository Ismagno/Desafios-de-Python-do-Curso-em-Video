#CONTADOR DE DESCONTO
print('===== CONTADOR DE DESCONTO =====')
p1 = float(input('Qual o preço? '))
d = float(input('Quanto é o desconto: '))
#dr = d/100
pd = p1-(p1*(d/100))
#print('O produto de {} R$ está a {:.2f}R$ com os {}% de desoconto aplicado'.format(p1, pd, d))
print(f'o produto de {p1} R$ está a {pd:.2f}R$ com os {d}% de desconto aplicado')