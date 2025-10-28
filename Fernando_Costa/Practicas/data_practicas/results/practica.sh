#!/bin/bash
echo "Iniciando el script..."
mkdir cosita
cd cosita
curl https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/2016-weather-data-seattle.csv > data3.csv 
echo "Todo listo!"