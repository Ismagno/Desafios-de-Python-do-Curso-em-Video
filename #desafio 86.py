#desafio 86 

matriz = []

for linha in range(0, 3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        matriz.append(valor)

print('=-'*30)
for i, v in enumerate(matriz):
    print(f'[ {matriz[i]} ]', end = ' ' if (i+1) % 3 != 0 else '\n' )