# Python std lib: https://docs.python.org/3/library/index.html
import random
import math
import datetime

# random bibliotēka - nejauši skaitļi, varbūtības sadalījumi
x = 1
y = 10
skaitlis = random.randint(x, y) # Atgriež nejaušu skaitli diapazonā no x, līdz y

# math bibliotēka - matemātiskās funckijas, piem. kosīnuss, tangens, logaritmi u.tml.
skaitlis = math.floor(10.5) # noapaļo skaitli uz leju = 10.5 => 10
skaitlis = math.ceil(10.5) # noapaļo skaitli uz augšu = 10.5 => 11

# datetime bibliotēka - darbs ar laiku
# iedalās apakšbibliotēkās - datetime (laiks un datums), date (datums) un time (laiks)
datums = datetime.datetime.now()
print(datums)

# Izskatīsim vēlāk, kad par tām būs tēma
#import os - darbs ar mapēm, failiem
#import shutil - darbs ar mapēm, failiem
#import csv - darbs ar datubāzēm
#import sqlite3 - darbs ar datubāzēm

# Trešās partijas bibliotēkas - varam instalēt manuāli
# Lai instalētu bibliotēkas - komanda pip terminālī!
# pip install <bibliotēkas nosaukums>, piem. pip install matplotlib
# Bibliotēkas nosaukumus var atrast python bibliotēku sarakstā šeit - https://pypi.org/
# Vieglākais veids kā atrast - googlē vai citā meklēšanas dzinī meklējam
# "python <ko vajag> library", piem. ja gribam grafikas bibliotēku - "python 2D graphics library"
# Vai arī virtuālajās vidēs - uv, venv komandas (šo mēs klasē neizskatām)

# Pēc matplotlib uzinstalēšanas varam pamēģināt šo bibliotēku
# import matplotlib.pyplot as plt
# import numpy as np
# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
# fig, ax = plt.subplots()
# ax.plot(t, s)
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
# fig.savefig("test.png")
# plt.show()

# Pastāvīgs uzdevums:
# Uzinstalēt bibliotēku 'requests' (pip install)
# Atrast piemēru kā to lietot (requests.get(...), print(rezultāts.text))
# Un iegūt sekojošo mājaslapu izmantojot python kodu, izvadīt rezultātu 
# https://api.sampleapis.com/coffee/hot
import requests
r = requests.get('https://api.sampleapis.com/coffee/hot')
print(r.text)