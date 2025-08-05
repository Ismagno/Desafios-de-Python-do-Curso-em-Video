#desafio 85

lista = []
par = []
impar = []

for v in range (1, 8):
    n = (int(input(f'{v}º valor: ')))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.append(par[:])
lista.append(impar[:])
lista[0].sort()
lista[1].sort()
print('-'*30)
print('Os valores pares digitados foram ', end='')
for i, v in enumerate(lista[0]):
    print(v, end=', ' if i < (len(lista[0])-1) else '\n')
print('Os valores impares digitados foram ', end='')
for i, v in enumerate(lista[1]):
    print(v, end=', ' if i < (len(lista[1])-1) else '\n')
