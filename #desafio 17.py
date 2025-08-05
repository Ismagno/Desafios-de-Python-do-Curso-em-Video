#Teorema de pitagoras
import math
print('='*20)
print('Calcular a hipotenusa: ')
ca = float(input('Infome o cateto adjacente: '))
co = float(input('Informe o cateto oposto: '))
h = math.hypot(co, ca)
print(f'De acordo com os catetos {ca} e {co} a hipotenusa é igual a {h:.2f}')
print('='*20)
print('Para finaliza o progama aperte ENTER!')