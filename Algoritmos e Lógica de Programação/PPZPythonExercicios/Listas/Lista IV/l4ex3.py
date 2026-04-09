import random
 
print('Sorteio de dez valores em duas lista e lista intercalando valores')
print()
 
valoresRandom = []
valoresRandom2 = []
valoresRandom = random.sample(range(1,101), 10)
valoresRandom2 = random.sample(range(1,101), 10)
 
print(f'Valores sorteados (primeira lista): {valoresRandom}.')
print()
print(f'Valores sorteados (segunda lista): {valoresRandom2}.')
print()
 
listaFinal = []
 
for valor in zip(valoresRandom, valoresRandom2):
    listaFinal.extend(valor)
 
print(f'Lista final: {listaFinal}.')
