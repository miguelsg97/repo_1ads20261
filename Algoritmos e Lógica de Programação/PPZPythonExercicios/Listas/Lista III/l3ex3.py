print('Estimativas com taxas de crescimento')
print()
paisA = 80000
paisB = 200000
paisA = int(paisA)
paisB = int(paisB)
taxaA = 0.03
taxaB = 0.015
anos = 0
print(f'População atual do país A: {paisA}')
print(f'População atual do país B: {paisB}')
print(f'Taxa de crescimento atual do país A: {(taxaA * 100)}%')
print(f'Taxa de crescimento atual do país B: {(taxaB * 100)}%')
print()
while paisA < paisB:
    paisA = int(paisA + paisA * taxaA)
    paisB = int(paisB + paisB * taxaB)
    anos = anos + 1
print(f'Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.')
