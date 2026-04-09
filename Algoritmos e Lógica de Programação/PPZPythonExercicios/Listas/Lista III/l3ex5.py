print('MDC com Algoritmo de Euclides')
print()
n1 = int(input('Insira um valor inteiro positivo: '))
while n1 <= 0:
    print()
    print('O valor inserido NÃO é aceito. Tente novamente.')
    print()
    n1 = int(input('Insira um valor inteiro positivo: '))
n2 = int(input('Insira mais um valor inteiro positivo: '))
while n2 <= 0:
    print()
    print('O valor inserido NÃO é aceito. Tente novamente.')
    print()
    n2 = int(input('Insira mais um valor inteiro positivo: '))
while ((n1 % n2) > 0):
    resto = n1 % n2
    n1 = n2
    n2 = resto
print()
print('O MDC é igual a: ', n2)
