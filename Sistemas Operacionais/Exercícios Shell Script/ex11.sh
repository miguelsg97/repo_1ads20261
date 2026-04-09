#!/bin/bash

clear
read -p 'Informe o PID (ID do processo) do processo a ser finalizado: ' processpid

echo

if kill -9 "$processpid"; then
	echo 'Processo finalizado!'
else
	echo 'Processo NÃO finalizado, verifique o PID.' 
fi