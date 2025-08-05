#conversor de temperaturas 
print('-'*30)
c = float(input('Informe a temperatura em Celsius: '))
f = (c*(9/5))+32
k = c + 273
print(f'{c:.2f}°C é equivalente a {f:.2f}°F e a {k:.2f} K')
print('-'*20)
input('Aperte ENTER para sair !')
