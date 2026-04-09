#!/bin/bash

clear

read -p 'Informe o caminho do arquivo cujas permissões devem ser alteradas: ' filename
read -p 'Informe o número da permissão a ser atribuída: ' perm

echo

chmod "$perm" "$filename"

echo

echo "Permissão de $filename alterada!"