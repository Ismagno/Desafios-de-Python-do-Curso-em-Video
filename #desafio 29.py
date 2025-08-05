#desafio 29
print('===== DETRAN =====')
v = float(input('Qual a velocidade você estava(Km/h): '))
if v > 80: 
    multa = (v-80)*7
    print('Você foi multado em {:.2f}R$ por passar a {:.2f}Km/h, em via não permitida'.format(multa,v))
else:
    print('Você estava dentro do limite de velocidade, muito bem!')
print('------FIM------')