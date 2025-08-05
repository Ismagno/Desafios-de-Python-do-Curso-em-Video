#desafio 78.2
from random import randint

valores = list()

for c in range(1, 6):
    valores.append(randint(1, 10))
vmax = max(valores)
vmin = min(valores)
print(f'Os valores são: ')
for i, v in enumerate(valores):
    print(f'{i+1}º {v}')
print('-'*30)
print(f'O maior valor é {vmax} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == vmax:
        print(i+1, end = '... ')

print(f'\nO menor valor é {vmin} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == vmin:
        print(i+1, end ='... ')