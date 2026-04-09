print('Cálculo de aumento de salário')
print('Insira as informações requisitadas a seguir.')
print()
salarioBase = float(input('Salário base: '))
porcentagemAumento = float(input('Porcentagem do aumento: '))
valorAumento = salarioBase * porcentagemAumento / 100
salarioNovo = salarioBase + valorAumento
print()
print(f'Valor do aumento: R${valorAumento:.2f}')
print(f'Novo salário: R${salarioNovo:.2f}')
