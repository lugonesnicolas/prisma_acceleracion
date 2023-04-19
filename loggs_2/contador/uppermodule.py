import logging
import contador.lowermodule as lowermodule

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s  %(name)s %(levelname)s:%(message)s',datefmt="%Y-%m-%dT%H:%M:%S%z")
logger=logging.getLogger(__name__)

def record_word_count(myfile):
    logger.info("Starting the function")
    try:
        word_count=lowermodule.word_count(myfile)
        with open('wordcountarchive.csv', 'a') as file:
            row=str(myfile) + ',' + str(word_count)
            file.write(row + '\n')
    except:
        logger.warning("Cloud not write file %s to destination", myfile)
    finally:
        logger.debug("The function is done for the file %s", myfile)
        
def main():
    record_word_count('texto_prueba.txt')
        
if __name__ == '__main__':
    main()