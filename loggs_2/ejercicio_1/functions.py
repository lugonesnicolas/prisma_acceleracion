def contar_lineas_palabras():
    with open ("cuento.txt", 'r') as f: #Abrimos el archivo
        for i in f: #Recorre las lineas
            result=len(i.split())
            print(i, result)

    

if __name__=="__main__":
    contar_lineas_palabras()