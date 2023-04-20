import logging
import logging.config

#Import file.conf
logging.config.fileConfig('log_config_file.conf')

#Create loggers
logger_functions=logging.getLogger('functions')
logger_main=logging.getLogger('main')


"""Contador cuenta renglones y palabras
cuento: TextIOWrapper
return: None
"""        
def contador(cuento):
    nombre=cuento.name #Nombre del cuento
    contenido=cuento.read() #Convertimos a string
    renglones_list=contenido.split("\n") #Separamos los renglones en listas
    renglones=len(renglones_list) #Contamos los renglones
    logger_functions.info('%s - Cantidad de renglones: %s', nombre, renglones) #Log cantidad de renglones
    contador=0 #Contador de renglones para encadenar la cantidad de palabras
    for i in renglones_list: #Recorremos los renglones que estan en la lista
        palabras=len(i.split(" ")) #Leemos la cantidad de palabras
        logger_functions.info('Renglon %s: %s palabras', contador, palabras) #Logs renglon y su cantidad de palabras
        contador+=1