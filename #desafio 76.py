#desafio 76
print('-'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('-'*35)

lista = ('Lápis' , 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Celular', 200)
cont = 0

while True:
    print('{:.<26}R$ {:>6.2f}'.format(lista[cont], lista[cont+1]))
    cont +=2
    if cont == len(lista):
        break
print('-'*35)

