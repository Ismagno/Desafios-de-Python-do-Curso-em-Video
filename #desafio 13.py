#DESAFIO 13
d = ('DESAFIO 13')
print('{:=^20}'.format(d))
s = float(input('Qual o seu salário? '))
a = float(input('Quantos % de aumento? '))
#CONTAS
ar = a/100
sr = s + (s*ar)
diferença = sr - s
print('O seu salário teve um aumento de {:.2f}R$, logo seu salário agora é {:.2f}R$, apois o reajuste de {}% ! '.format(diferença, sr, a))
