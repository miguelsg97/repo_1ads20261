#!/bin/bash

clear

read -p 'Informe o caminho para o arquivo a ser lido: ' filegrep
read -p 'Informe a palavra ou frase a ser buscada: ' words

echo

if grep "$words" "$filegrep"; then
	echo "$words encontrado em $filegrep"
else
	echo "$words NÃO encontrado em $filegrep"
fi