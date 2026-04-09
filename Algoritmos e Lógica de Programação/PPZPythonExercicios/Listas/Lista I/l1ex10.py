print('Cálculo da redução do tempo de vida de um fumante')
print('Informe valores a seguir.')
print()
qtdCigarros = int(input('Quantidade de cigarros fumados diariamente: '))
anosFumando = float(input('Quantidade de anos fumando: '))
diasPerdidos = ((10 * qtdCigarros) * 365 * anosFumando) / 1440
diasPerdidos = round(diasPerdidos)
print()
print('Dias de vida perdidos em decorrência do cigarro: ', diasPerdidos)
