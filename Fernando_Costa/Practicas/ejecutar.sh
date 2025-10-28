#!/bin/bash
echo "Iniciando el script..."
mkdir data
cd data
curl https://gist.githubusercontent.com/RobVanGroenewoud/ba89ad7684df8cefe5c183adb498cc65/raw/f2eec6d2cb89f5d779e16b28ed0dab89d738ba96/sample.csv > archivo.csv
mkdir data2
cp archivo.csv data2/data_descargado.csv
rm archivo.csv
start data2/data_descargado.csv
echo "Todo listo!"
echo Hola $1!