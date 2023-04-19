#ejercicio1.py
import logging

fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]

for i in fruits:
    if type(i)==str:
        # print(type(i))
        print(i,'se puede convertir')
    else:
        print(i,'No se puede convertir')