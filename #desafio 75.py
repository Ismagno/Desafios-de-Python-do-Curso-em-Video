#desafio 75
n1 = int(input('1º Valor: '))
n2 = int(input('2º Valor: '))
n3 = int(input('3º Valor: '))
n4 = int(input('4º Valor: '))
num = (n1, n2, n3, n4)

print(f'Os valores digitados foram: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados são: ', end= '')
for c in range(0, len(num)):
    if num[c] % 2 == 0:
        print(num[c], end = ' ')