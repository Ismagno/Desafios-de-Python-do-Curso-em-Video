#desafio 74
from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
cont = 0

print(f'Os valores sorteados são: {num}')
print(f'O maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')