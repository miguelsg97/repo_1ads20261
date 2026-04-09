print('Cálculo de troco')
print()
valorConta = int(input('Insira o valor da conta a ser paga: '))
valorPagamento = int(input('Insira o valor do pagamento efetuado: '))
print()
valorTroco = valorPagamento - valorConta
notas = [50, 20, 10, 5, 2, 1]
if valorPagamento > valorConta:
    for nota in notas:
        qtdNotas = valorTroco // nota
        if qtdNotas > 0:
            print(f'Devolva {qtdNotas} nota(s) de R${nota}.')
            valorTroco %= nota
elif valorConta == valorPagamento:
    print('Não há troco a ser devolvido.')
else:
    valorDevendo = valorConta - valorPagamento
    print(f'O pagador ainda deve R${valorDevendo}.')
