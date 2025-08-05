#desafio 80
valores = list()

for c in range(1, 6):
    n = int(input(f'{c}º valor: '))
    if c == 1:
        valores.append(n)
        print('Número adicionado no final da lista')
    else:
        for i, v in enumerate(valores):
            if n > v:
                valores.append(n)
                print('Número adicionado no final da lista')
            elif n <= v:
                valores.insert(i, n)
                print(f'Número adicionado na posicão {i}')
    
print(f'Valores em ordem {valores}')