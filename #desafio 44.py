#desafio 44
print('='*30)
p = float(input('Qual o preço do produto? '))
c = int(input('Qual o metodo de pagamento?\n1 - À VISTA\n2 - À VISTA NO CARTÃO\n3 - 2x NO CARTÃO\n4 - 3x OU MAIS VEZES NO CARTÃO:\n'))
if c == 1:
    print('O produto fica no valor de R$ {:.2f} com 10% de desconto!'.format(p - (p * 0.1)))
elif c == 2:
    print('O produto fica no valor de R$ {:.2f} com 5% de desconto!'.format(p - (p * 0.05)))
elif c == 3:
    print('É possivel pagar em 2x de R$ {:.2f} sem juros!'.format(p/2))
elif c == 4:
    par = int(input('Quantas parcelas? '))
    acr = ((p * 0.2) + p)
    print('O produto fica no valor de R$ {:.2f} com 20% de acréscimo!'.format(acr))
    if par >= 3:
        print('As parcelas ficam R$ {} de {} vezes'.format((acr/par),par))
else:
    print('Opção invalida de pagamento')
print('Volte sempre!')  