#desafio 89

lista = []

while True:
    print(f'{len(lista)+1}º PESSOA')
    nome = str(input('NOME: '))
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    lista.append([nome, [n1,n2], ((n1+n2)/2)])
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f'{" AlUNOS ":=^30}')
print(f'{"NO.":<6}{"NOME":<20}{"MÉDIA":>4}')
for i, v in enumerate(lista):
    print(f'{(i+1):<6}{v[0]:<20}{v[2]:>4.1f}')
while True:
    print('='*30)
    while True:
        aluno = int(input('Quer ver nota de qual aluno? [999 exit] '))
        if 0 < aluno <= (len(lista)) or aluno == 999:
            break
        else: 
            print('Aluno Invalido... Tente novamente!')
    if aluno == 999:
        break
    print(f'{lista[(aluno)-1][0]} teve as notas {lista[(aluno)-1][1]}')
print('='*30)
