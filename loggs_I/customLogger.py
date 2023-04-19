#customLogger.py
import logging

#Creamos el logger personalizado
logger=logging.getLogger(__name__)

#Nivel de severidad
logger.setLevel(logging.DEBUG)

#Creamos los handlers
handler_1=logging.StreamHandler()
handler_2=logging.FileHandler('logs.txt')

#Nivel de severidad de los handlers
handler_1.setLevel(logging.WARNING)
handler_2.setLevel(logging.ERROR)

#Formato e integracion a cada handler
handler_1_format=logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler_2_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_1.setFormatter(handler_1_format)
handler_2.setFormatter(handler_2_format)

#Agregamos los handlers al logger
logger.addHandler(handler_1)
logger.addHandler(handler_2)

#Probamos eL Logger personalizado
logger.warning( 'Esto es un warning')
logger.error( 'Esto es un error')