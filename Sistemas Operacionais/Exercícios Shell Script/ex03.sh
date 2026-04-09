#!/bin/bash

clear

read -p 'Informe o nome do arquivo a ser renomeado: ' filemv
read -p 'Informe o nome desejado: ' novonome
read -p 'Informe o caminho para o arquivo: ' dir

cd "$dir"
mv "$filemv" "$novonome"

echo

echo 'Arquivo renomeado!'