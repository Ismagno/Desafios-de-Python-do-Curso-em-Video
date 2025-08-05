#desafio 43
print('====== IMC ======')
p = float(input('Qual seu peso?(kg) '))
a = float(input('Qual sua altura?(m) '))
imc = p/(a**2)
if imc < 18.5:
    print('Você está abaixo do peso ideal, seu IMC é {:.2f}'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal, seu IMC é {:.2f}'.format(imc))
elif imc > 25 and imc < 30:
    print('Você está com SOBREPESO, seu IMC é {:.2f}'.format(imc))
elif imc > 30 and imc < 40:
    print('Você está com OBSIDADE, seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com OBSIDADE MOÓRBIDA, seu IMC é {:.2f}'.format(imc))
print('SEMPRE MUITO IMPORTANTE CUIDAR DA SAÚDE!!')
print('='*17)