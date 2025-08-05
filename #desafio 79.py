#desafio 79

valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN': 
            break
    if continuar == 'N':
        break
print('-'*30)
valores.sort()
print(f' Os valores digitados foram {valores}') 
