#desaio 48
print('{:=^30}'.format(' ÍMPARES E MULTIPLOS DE 3 '))
s = 0
cont = 0
for c in range(1, 501, 2):
    r = c % 3
    if r == 0:
        cont += 1
        s += c
print('A soma dos {} números é igual a {}'.format(cont,s))