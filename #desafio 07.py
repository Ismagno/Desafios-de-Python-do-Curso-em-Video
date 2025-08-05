#DESAFIO 07
print('===== DESAFIO 7 =====')
nome = input('Nome do aluno: ')
nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))
media = (nota1 + nota2)/2
print('As notas do aluno {}, são {} e {}, logo sua média é {:.1f}!'.format(nome, nota1, nota2, media))