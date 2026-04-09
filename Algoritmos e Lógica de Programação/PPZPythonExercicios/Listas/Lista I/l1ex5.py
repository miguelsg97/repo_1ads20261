print('Cálculo de preços de mercadorias e descontos')
print('Digite valores a seguir.')
print()
valorMercadoria = float(input('Valor da mercadoria: '))
percentualDesconto = float(input('Percentual do desconto: '))
valorDesconto = valorMercadoria * percentualDesconto / 100
valorFinalMercadoria = valorMercadoria - valorDesconto
print()
print(f'Valor do desconto: R${valorDesconto:.2f}')
print(f'Valor final da mercadoria:  R${valorFinalMercadoria:.2f}')
