import logging

"""Logs por consola"""
# logging.basicConfig(level=logging.DEBUG)

"""Logs en un archivo app.log"""
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='app.log',
#     filemode='w',
#     format='%(name)s - %(levelname)s - %(message)s'
# )

"""Ejercicion 1 - Imprimir por consola Warnings"""
# logging.basicConfig(
#     level=logging.WARNING,
#     format='%(name)s - %(levelname)s - %(message)s'
# )

"""Ejercicio 2 - Exportar en un archivo txt"""
logging.basicConfig(
    level=logging.ERROR,
    filename='logs.txt',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug('Este es un mensaje de debbug')
logging.info('Este es un mensaje de informacion')
logging.warning('Este es un mensaje de warning')
logging.error('Este es un mensaje de error')
logging.critical('Este es un mensaje critico')
