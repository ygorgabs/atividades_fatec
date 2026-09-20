# -*- coding: utf-8 -*-

import os # SCRIPT1.PY
import time
import sys

sexo = ''
msg = ''

os.system('clear')
sexo = input('Digite o sexo M/F: ')

if sexo == 'F':
    msg = 'vc é uma mulher'
else:
    msg = 'vc é um homem'

os.system('clear')
print (msg)
time.sleep(5)
sys.exit # sai do programa