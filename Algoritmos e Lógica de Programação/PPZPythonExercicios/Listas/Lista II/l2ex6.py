print('Cálculo de salário e descontos')
print()
print('Insira valores a seguir: ')
print()
valorHora = float(input('Valor recebido por hora: '))
horas = int(input('Horas trabalhadas (mês): '))
if valorHora < 0 or horas < 0:
    print('Os valores não podem ser negativos. Tente novamente.')
else:
    salarioBruto = valorHora * horas
    impostoRenda = salarioBruto * 0.11
    inss = salarioBruto * 0.08
    sindicato = salarioBruto * 0.05
    descontosTotais = impostoRenda + inss + sindicato
    salarioLiquido = salarioBruto - descontosTotais
    print()
    print(f'Salário bruto: R${salarioBruto:.2f}')
    print(f'Desconto Imposto de Renda: R${impostoRenda:.2f}')
    print(f'Desconto INSS: R${inss:.2f}')
    print(f'Desconto sindicato: R${sindicato:.2f}')
    print(f'Descontos totais: R${descontosTotais:.2f}')
    print(f'Salário líquido: R${salarioLiquido:.2f}')
