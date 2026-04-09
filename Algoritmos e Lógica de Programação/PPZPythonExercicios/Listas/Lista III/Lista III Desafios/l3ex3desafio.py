print('Cálculo de números primos')
print()
n = int(input('Insira um número: '))
print()
if n == 1:
    print('O número inserido NÃO é primo.')
elif n <= 0:
    print('O número inserido não é um inteiro positivo, logo, NÃO é primo.')
else:
    ct = 1
    ac = 0
    while ct <= n:
        if n % ct == 0:
            ac += 1
        ct += 1
    if ac == 2:
        print('O número inserido É primo.')
    else:
        print('O número inserido NÃO é primo.')
