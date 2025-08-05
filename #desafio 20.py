#sorteador da ordem de alunos
import random
n1 = str(input('ALUNO 1: '))
n2 = str(input('ALUNO 2: '))
n3 = str(input('ALUNO 3: '))
n4 = str(input('ALUNO 4: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'A ordem de apresentação é: ', end='')
for lista in lista:
   print(f'{lista},', end=' ')