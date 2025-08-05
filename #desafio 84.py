#desafio 84

lista =[]
pessoas = []
pmax = []
pmin = []

while True:
    print(f'{(len(lista)+1)}ª Pessoa ')
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    lista.append(pessoas[:])
    pessoas.clear()
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
    print('-'*30)
    if resposta == 'N':
        break

print(f'Foram cadastradas {len(lista)} pessoas!')

for v in lista:
    if v[1] >= 100:
        pmax.append(v[0])
    elif v[1] <= 70:
        pmin.append(v[0])
if pmax:  
    print('As pessoas mais pesadas são : ', end='')
    for i,v in enumerate(pmax):
        print(v, end =', ' if i < (len(pmax)-1) else '\n')
else:
    print('Não tem pessoas acima de 100Kg')

if pmin:
    print('As pessoas mais leves são : ', end='')
    for i, v in enumerate(pmin):
        print(v, end =', ' if i < (len(pmin)-1) else '\n')
else:
    print('Não tem pessoas abaixo de 70Kg')