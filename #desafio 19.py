#nome de pessoas radom D19
import random
print('='*30)
print('Quem vai apagar o quadro? ')
n1 = str(input('ALUNO 1: '))
n2 = str(input('ALUNO 2: '))
n3 = str(input('ALUNO 3: '))
n4 = str(input('ALUNO 4: '))
lista = [n1,n2,n3,n4]
print('O aluno selecionado é',random.choice(lista))