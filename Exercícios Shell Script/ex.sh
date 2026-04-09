#!/bin/bash

clear

read -p 'Primeiro valor: ' v
 read -p 'Segundo valor: ' v2

echo

echo '1. Somar
2. Subtrair
3. Multiplicar
4. Dividir'

echo

read -p 'Insira a opção desejada: ' op

echo

case $op in
	1)
   	soma=expr $v + $v2
		echo "Valor final: $soma"
		;;
	2)
     subtracao=expr $v - $v2
		echo "Valor final: $subtracao"
		;;
	3)
     multi=expr $v \* $v2
     echo "Valor final: $multi"
     ;;
	4)
     divisao=$(echo "scale=2; $v / $v2" | bc)
		echo "Valor final: $divisao"
     ;;
	*)
		echo "Opção inválida."
esac