print('Descobrindo a quantidade de valores pares e divisíveis por 7 entre 1067 e 3627')
print()

cont = 0

for i in range(1067, 3628):
    if i % 14 == 0:
        cont += 1

print(f'Quantidade de valores pares e divisíveis por 7: {cont}')