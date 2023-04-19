import logging

"""Logs por consola"""
# logging.basicConfig(level=logging.DEBUG)

"""Logs en un archivo app.log"""
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)


logging.debug('Este es un mensaje de debbug')
logging.info('Este es un mensaje de informacion')
logging.warning('Este es un mensaje de warning')
logging.error('Este es un mensaje de error')
logging.critical('Este es un mensaje critico')