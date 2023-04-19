#ejercicio1.py
import logging

"""Logs en un archivo app.log"""
logging.basicConfig(
    level=logging.DEBUG,
    filename='result.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

#Lista a trabajar
fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]

#Recorremos y si es posible convertir a minuscula mostramos
# for i in fruits:
#     if type(i)==str:
#         minuscula=i.lower()
#         logging.info("Conversion exitosa: %s ---> %s", i, minuscula)
#     else:
#         logging.error("Conversion fallida: %s", i)
        
for i in fruits:
    try:
        if type(i)==str:
            minuscula=i.lower()
            logging.info("Conversion exitosa: %s ---> %s", i, minuscula)
        else:
            raise ValueError
        
    except ValueError:
        logging.error("Conversion fallida: %s", i)