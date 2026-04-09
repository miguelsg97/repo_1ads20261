print('Inversão de números')
print()
n = int(input('Insira um número: '))
inversao = 0
print()
while n > 0:
    ud = n % 10
    inversao = inversao * 10 + ud
    n //= 10
print(f'Número invertido: {inversao}')
