#desafio 87

matriz= []
par = 0
soma3 = 0
linha2 = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        valor = int(input(f'Digite o valor [{linha}, {coluna}]: '))
        if linha == 1:
            linha2.append(valor)
        matriz.append(valor)

for i, v in enumerate(matriz):
    if v % 2 == 0:
        par += v
    if (i+1) % 3 == 0:
        soma3 += v
        
print('='*30)
print(f'A soma de todos os valores pares {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {max(linha2)}')
print('='*30)