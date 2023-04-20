import logging
import logging.config

logging.config.fileConfig('log_config_file.conf')

#Create logger
logger=logging.getLogger('functions')


def contar_renglones(cuento):
    nombre=cuento.name
    renglones=0
    for i in cuento:
        renglones+= 1
    logger.info('%s - Cantidad de renglones: %s', nombre, renglones) #Logs renglon palabras


def contar_lineas_palabras(cuento):
    renglon=0
    for i in cuento: #Recorre las lineas
        palabras=len(i.split()) #Palabras por renglon
        logger.info('Renglon %s: %s palabras', renglon, palabras) #Logs renglon palabras
        renglon+= 1