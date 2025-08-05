#desafio 27
print('='*40)
n = str(input('Qual é o seu nome completo? ')).strip().title()
nome = n.split()
print('O seu primeiro nome é : {}\nSeu último nome é : {}'.format(nome[0], nome[len(nome)-1]))

