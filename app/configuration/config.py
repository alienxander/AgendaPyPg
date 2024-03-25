from configparser import ConfigParser
import os

def config(filename='pg.ini', section='postgresql'):
    parser = ConfigParser()
    
    with open(os.path.abspath(filename)) as fp:
        parser.read_file(fp)
    
    db = {}
    
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Seccion {section} no encontrada en el {filename} fichero.')

    return db