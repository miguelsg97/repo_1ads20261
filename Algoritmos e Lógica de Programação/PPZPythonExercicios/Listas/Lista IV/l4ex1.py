import random
 
print('Sorteio de dez valores; maior e menor valor')
print()
 
valoresRandom = []
valoresRandom = random.sample(range(1,101), 10)
 
print(f'Valores sorteados: {valoresRandom}.')
print()
 
maior = valoresRandom[0]
menor = valoresRandom[0]
 
for valor in valoresRandom:
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
 
print(f'Maior valor: {maior}; menor valor: {menor}.')
