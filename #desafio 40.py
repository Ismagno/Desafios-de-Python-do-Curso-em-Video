#desafio 40
print('===== MÉDIA =====')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('='*30)
m = (n1 + n2) /2
if m < 5:
    print('O aluno está reprovado!\nMédia igual a {:.1f}'.format(m))
elif m >= 5 and m <= 6.9:
    print('O aluno está de recuperação!\nMédia igual a {:.1f}'.format(m))
elif m >= 7:
    print('O aluno está aprovado!\nMédia igual a {:.1f}'.format(m))
    if m >= 9:
        print('PARABÉNS SUPER MÉDIA!!!!')
print('='*30)