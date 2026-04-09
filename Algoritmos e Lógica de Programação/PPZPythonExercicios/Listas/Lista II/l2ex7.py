print('Cálculo para pintura')
print()
print('Responda a seguir')
print()
area = float(input('Área a ser pintada (m²): '))
print()
if area <= 0:
    print('A área não pode ser negativa. Tente novamente.')
else:
    cobertura = area / 3
    qtdLatas = cobertura / 18
    qtdLatasFinal = -(-qtdLatas // 1)
    valorFinal = qtdLatasFinal * 80
    print('Quantidade de latas a serem compradas: ', qtdLatasFinal)
    print()
    print(f'Valor final: R${valorFinal:.2f}')
