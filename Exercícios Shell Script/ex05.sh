#!/bin/bash

clear

read -p 'Informe o nome do usuário a ser checado: ' username

echo

if id "$username"; then
	echo "O usuário $username existe no sistema."
else
	echo "O usuário $username NÃO existe no sistema."
fi
