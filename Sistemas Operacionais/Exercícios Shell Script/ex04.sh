#!/bin/bash

clear

read -p 'Informe o caminho para o arquivo: ' diratual
read -p 'Informe o caminho para o qual deseja movê-lo: ' novodir

mv "$diratual" "$novodir"

echo

echo 'Arquivo movido!'