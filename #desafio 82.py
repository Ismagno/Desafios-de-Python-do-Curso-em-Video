#desafio 82
cont =1
valores = list()
par = list()
impar = list()

while True:
    valores.append(int(input(f'{cont}º valor: ')))
    cont +=1
    while True:
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
for v in valores:
    if v % 2 == 0 and v != 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares são: {par}')
print(f'Os valores impares são: {impar}')
