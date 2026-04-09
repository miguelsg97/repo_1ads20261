print('Cálculo com a Sequência de Fibonacci')
print()
n = int(input('Insira um valor inteiro: '))
n1, n2 = 1, 1
contador = 1
print()
while n <= 0:
    print()
    print('O valor inserido é inválido. Tente novamente.')
    print()
    n = int(input('Insira um valor inteiro: '))
while contador <= n-2:
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    contador = contador + 1
print(f'Número de Fibonacci: {n2}')
