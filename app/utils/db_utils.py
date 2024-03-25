import psycopg2
from app.configuration.config import config
from app.exceptions import ConnectionException
from abc import ABC, abstractmethod

class DB(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__conn = None
    
    @abstractmethod
    def get_connection(self):
        pass
    
    def close_connection(self):
        if self.__conn is not None:
            self.__conn.close()
            print("Conección PostgreSQL Cerrada")

class PostgreSQL(DB):
    
    def __init__(self) -> None:
        super().__init__()
    
    def get_connection(self):
        try:
            params = config()
            print('Conectando con PostgreSQL...')
            self.__conn = psycopg2.connect(**params)
            
            cur = self.__conn.cursor()
            
            cur.execute('SELECT version()')
            
            db_version = cur.fetchone()

            cur.close
            
            return db_version
        except psycopg2.DatabaseError as e:
            raise ConnectionException(menssage="Se ha producido un error al conectarse a la base de datos PostgreSQL.")
        except Exception as e:
            raise ConnectionException(menssage=e)        
        finally:
            print("Fin get_connect()..")
            
    def close_connection(self):
        self.__close_connection()