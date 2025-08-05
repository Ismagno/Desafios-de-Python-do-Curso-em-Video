#desafio 50
s = 0
cont = 0
for c in range(1, 7):
    n = int(input('{}º Número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('A soma dos {} números pares é {}'.format(cont,s))