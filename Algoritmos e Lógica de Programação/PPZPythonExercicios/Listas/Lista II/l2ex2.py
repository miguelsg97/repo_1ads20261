print('Cálculo de Ano Bissexto')
print()
ano = int(input('Insira o ano: '))
print()
if ano < 0:
    print('O valor inserido é inválido.')
elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano é bissexto.')
else:
    print('O ano NÃO é bissexto.')
