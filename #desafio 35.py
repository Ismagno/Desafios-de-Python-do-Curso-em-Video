#desafio 35
print('='*30)
print('Forneça três comprimentos de retas: ')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
sr = r1 + r2
if sr < r3:
    print('Não é possivel fazer um trinagulo!')
    print('A soma das retas({:.2f}) é maior que o terceiro lado({:.2f})'.format(sr,r3))
else:
    print('É possivel fazer um triângulo!')
    print('A soma das retas({:.2f}) é menor que que o terceiro lado({:.2f})'.format(sr,r3))
