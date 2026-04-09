print('Descubra o maior e o menor número')
print()
n = float(input('Insira o 1º valor: '))
n2 = float(input('Insira o 2º valor: '))
n3 = float(input('Insira o 3º valor: '))
print()
if n >= n2 and n >= n3:
    maior = n
elif n2 >= n and n2 >= n3:
    maior = n2
else:
    maior = n3
if n <= n2 and n <= n3:
    menor = n
elif n2 <= n and n2 <= n3:
    menor = n2
else:
    menor = n3
print(f'O menor valor é', menor)
print(f'O maior valor é', maior)
