#desafio 34
print('====  AUMENTO SALARIAL =====')
s = float(input('Qual o seu salário: '))
if s > 1250:
    sn = s + (s*0.1)
    print('Seu novo salário é {:.2f} com um aumento de 10%'.format(sn))
else:
    sn = s + (s*0.15)
    print('Seu novo salário é {:.2f} com um aumento de 15%'.format(sn))