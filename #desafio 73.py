#desafio 73

tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 
          'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 
          'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 
          'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 
          'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá' 
)

print('Os cincos primeiro colocados: ')
for pos, time in enumerate(tabela[:5]):
    print(f'{pos+1:<2}º : {time}')
print('='*30)
print('O Z4 é composto por: ')
for pos, time in enumerate((tabela[16:]), start = 16):
    print(f'{pos+1:<2}º : {time}')
print('='*30)
#print(sorted(tabela))
for i, time in enumerate(sorted(tabela)):
    print(time, end = ', ' if i < (len(tabela)-1) else '\n')
print('='*30)
print('Flamengo está em {}º colocado'.format(tabela.index('Flamengo') + 1))