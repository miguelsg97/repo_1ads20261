print('Definição de números triangulares')
print()
n = int(input('Insira um número: '))
m1 = 0
m2 = 1
m3 = 2
ac = 0
print()
while ac < n:
    m1 += 1
    m2 += 1
    m3 += 1
    ac = m1 * m2 * m3
if ac == n:
    print(f'O número inserido É triangular ({m1} * {m2} * {m3} = {ac}).')
else:
    print('O número inserido NÃO é triangular.')
