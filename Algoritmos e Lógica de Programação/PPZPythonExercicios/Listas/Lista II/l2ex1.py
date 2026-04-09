print('Cálculo de Triângulos')
print()
valor = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
valor3 = float(input('Terceiro valor: '))
print()
if valor + valor2 > valor3 and valor + valor3 > valor2 and valor2 + valor3 > valor:
    if valor == valor2 and valor2 == valor3:
        print('O triângulo é equilátero.')
    elif valor == valor2 or valor == valor3 or valor2 == valor3:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Não forma um triângulo.')
