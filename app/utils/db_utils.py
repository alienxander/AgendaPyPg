import psycopg2
from app.configuration.config import config
from app.exceptions import ConnectionException
from abc import ABC, abstractmethod
from app.modelos import Animal

class DB(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._conn = None
    
    @abstractmethod
    def get_connection(self):
        pass
    
    def close_connection(self):
        if self._conn is not None:
            self._conn.close()
            print("Conección PostgreSQL Cerrada")

class PostgreSQL(DB):
    
    def __init__(self) -> None:
        super().__init__()
    
    def get_connection(self):
        try:
            params = config()
            print('Conectando con PostgreSQL...')
            self._conn = psycopg2.connect(**params)
            
            cur = self._conn.cursor()
            
            cur.execute('SELECT version()')
            
            db_version = cur.fetchone()

            cur.close
            
            return db_version, self._conn
        except psycopg2.DatabaseError as e:
            raise ConnectionException(menssage="Se ha producido un error al conectarse a la base de datos PostgreSQL.")
        except Exception as e:
            raise ConnectionException(menssage=e)        
        finally:
            print("Fin get_connect()..")
          
            
    def close_connection(self):
        super().close_connection()
        
        
class DBUtils:
    def __init__(self, conn) -> None:
        self.__conn = conn
        
    def get_animales(self) -> list:
        try:
                       
            cur = self.__conn.cursor()
            
            cur.execute('select nombre from public.animal')
            
            rows = cur.fetchall()
            
            #Creamos un bucle para imprimir los nombres
            lista_resultado: list = []
            for row in rows:
                print(row)
                animal = Animal(row[0])
                lista_resultado.append(animal)
                
            # Cerramos la comunicación con PostgreSQL

            cur.close
            
            return lista_resultado
        except psycopg2.DatabaseError as e:
            raise ConnectionException(menssage="Se ha producido un error al conectarse a la base de datos PostgreSQL.")
        except Exception as e:
            raise ConnectionException(menssage=e)        
        finally:
            print("Fin get_connect()..")