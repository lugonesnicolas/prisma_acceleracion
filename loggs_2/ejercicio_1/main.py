import functions as func

def main(cuento):
    try:
        func.logger_main.info('...Leyendo el archivo...')
        with open (cuento, 'r') as f: #Abrimos el archivo
            func.contador(f) #Contamos los renglones
            # func.contar_lineas_palabras(f) #Contamos las palabras por cada renglon
        func.logger_main.info('...Archivo procesado...')
    
    except ValueError:
        func.logger_main.error('No se pudo abrir el archivo')
        
if __name__=="__main__":
    main('cuento.txt')