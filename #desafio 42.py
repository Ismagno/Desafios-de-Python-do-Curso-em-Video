#desafio 42
print('===== TRIANGULO 2.0 =====')
print('Fonerça as retas para formar um triângulo: ')
r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É possivel formar um triângulo!')
    if r1 == r2 == r3:
        print('Este triângulo é Equilátero, todos os lados são iguais!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Este triângulo é Isósceles, a dois lados iguais!')
    else:
        print('Este triângulo é Escaleno, todos os lados direntes!')
else:
    print('Não é possivel formar um triângulo!')