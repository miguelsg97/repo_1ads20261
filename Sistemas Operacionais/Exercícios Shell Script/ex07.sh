#!/bin/bash

clear

echo 'Usuário logado : ' $(whoami)

echo 'Diretório principal (HOME):' $HOME

echo 'Espaço em disco utilizado por HOME:' $(du -sh $HOME)