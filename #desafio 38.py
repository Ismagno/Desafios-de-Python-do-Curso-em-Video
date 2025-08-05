#desafio 38
print('='*30)
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo valor ({n2})!')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior que o primeiro valor ({n1})!')
else:
    print(f'Os números são iguais!')
print('='*30)