#!/bin/bash
echo "Instaling"


sudo apt -y install python3 python3.10-venv finglet > /dev/null 2>&1


figlet 'Welcome to ConvergeCast Installation'
read x

python3 -m venv venv 
source venv/bin/activate

python3 -m pip install --upgrade pip
sudo apt update -y
sudo apt upgrade -y
python3 -m pip install -r requirements.txt
