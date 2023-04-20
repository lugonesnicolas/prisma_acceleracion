import logging
import logging.config
import functions as func

logging.config.fileConfig('log_config_file.conf')

#Create logger
logger=logging.getLogger('mainLogger')


def main():
    try:
        logger.info('...Leyendo el archivo...')
        with open ('cuento.txt', 'r') as f: #Abrimos el archivo
            func.contar_renglones(f) #Contamos los renglones
        with open ('cuento.txt', 'r') as f: #Abrimos el archivo
            func.contar_lineas_palabras(f) #Contamos las palabras por cada renglon
        logger.info('...Archivo procesado...')
    
    except ValueError:
        logger.error('No se pudo abrir el archivo')
        
if __name__=="__main__":
    main()