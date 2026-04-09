print('Descubra o maior número')
print()
n = float(input('Digite o primeiro número: '))
n2= float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print()
if n >= n2 and n >= n3:
    print(n, 'é o maior número.')
elif n2 >= n and n2 >= n3:
    print(n2, 'é o maior número.')
else:
    print(n3, 'é o maior número.')
