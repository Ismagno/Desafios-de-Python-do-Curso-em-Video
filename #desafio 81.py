#desafio 81

cont = 1
valores = list()
while True:
    valores.append(int(input(f'{cont}º valor: ')))
    cont +=1
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-'*30)
print(f'Você digitou {len(valores)} elementos! ')
valores.sort(reverse=True)
print(f'Os valores em ordem decressente são: {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista !')
else:
    print('O valor 5 não faz parte da lista !')