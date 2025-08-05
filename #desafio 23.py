#desafio 23
print('='*30)
n = int(input('Digite um numero de 0 a 9999: '))
print(f'O número {n} é composto por: ')
print(f'Unidade: {n//1%10}\nDezena: {n//10%10}\nCentena: {n//100%10}\nMilhar: {n//1000%10}')