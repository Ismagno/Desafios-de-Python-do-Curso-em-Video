#desafio 36
print('===== Compra de Casa =====')
nome = str(input('Nome completo: ')).strip().title()
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
anos = int(input('Quanto anos para pagar: '))
par = casa/(anos * 12)
cond = 0.3*salario
if cond <= par:
    print('{}, Você não pode fazer o emprésitmo !'.format(nome.split()[0]))
    print('A parcela da casa, {:.2f} R$, execede 30% do seu salário'.format(par))
else:
    print('Parabéns, {}, você pode fazer o empréstimo!'.format(nome.split()[0]))
    print('As parcelas ficaram {:.2f} R$ durante {} anos!'.format(par,anos))
print('Tenha um bom dia!')
print('='*30)