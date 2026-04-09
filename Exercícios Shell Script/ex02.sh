#!/bin/bash

clear

read -p 'Informe o nome do arquivo a ser removido: ' filerm
read -p 'Informe o caminho para o arquivo: ' dir

cd "$dir"
rm "$filerm"

echo

echo 'Arquivo deletado!'