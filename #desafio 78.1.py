#desafio 78.1

valores = list()

for c in range(1,6):
    valores.append(int(input(f'{c}º valor: ')))

vmax = max(valores)
vmin = min(valores)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {vmax} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == vmax:
        print(i+1, end = '... ')
print(f'\nO menor valor digitado foi {vmin} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == vmin:
        print(i+1, end = '... ')