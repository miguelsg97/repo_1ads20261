print('Números "sortudos" entre 18644 e 33087 (extremos incluídos)')
print()

cont = 0

for i in range(18644, 33088):
    s = str(i)
    if '2' in s and '7' not in s:
        cont += 1

print(f'Quantidade: {cont}')