print('Cálculo de Multa para Pescadores')
print()
kgPeixe = float(input('Informe o peso pescado: '))
print()
if kgPeixe > 50:
    excessoPeixe = kgPeixe - 50
    valorMulta = excessoPeixe * 4
else:
    excessoPeixe = 0
    valorMulta = 0
print(f'Excesso: {excessoPeixe:.2f} kg')
print(f'O valor da multa é de: R${valorMulta:.2f}')
