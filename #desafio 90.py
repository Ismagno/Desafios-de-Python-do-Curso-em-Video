#desafio 90

aluno = {}
aluno['Aluno'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Aluno"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'aprovado'
else:
    aluno['Situação'] =  'reprovado'
print('-'*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')