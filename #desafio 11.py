#desafio 11
print('===== DESAFIO 11 =====')
L = float(input('Qual a largura(m): '))
h = float(input('Qual a altura (m): '))
area = L*h
tinta = area/2
print('Será necessário {}L para pintar {}m²'.format(tinta, area))