#desafio 31
print('===== VIAGEM =====')
v = float(input('Vamos calcular sua passgagem!\nQuanto quilômetros é sua viagem? '))
if v <= 200 :
    p = v*(1/2)
else:
    p = v*(0.45)
print('Sua passagem custa {:.2f}R$'.format(p))