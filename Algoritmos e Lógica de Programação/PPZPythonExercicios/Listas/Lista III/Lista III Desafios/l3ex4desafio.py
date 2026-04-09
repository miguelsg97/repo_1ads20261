print('Decomposição em fatores primos e multiplicidade de fatores')
print()
n = int(input('Insira um valor: '))
print()
print('Fatores e multiplicidades:')
ct = 2
while n > 1:
    ac = 0
    while n % ct == 0:
        n //= ct
        ac += 1
    if ac > 0:
        print(ct, ac)
    ct += 1
