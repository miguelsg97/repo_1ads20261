import random
 
print('Sorteio de vinte valores; ímpares e pares')
print()
 
valoresRandom = []
valoresRandom = random.sample(range(1,101), 20)
 
print(f'Valores sorteados: {valoresRandom}.')
print()
 
impares = []
pares = []
 
for valor in valoresRandom:
    if valor % 2 != 0:
        impares.append(valor)
    else:
        pares.append(valor)
 
print(f'Valores ímpares: {impares};')
print()
print(f'Valores pares: {pares}.')
