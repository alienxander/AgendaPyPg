from app.utils.db_utils import PostgreSQL, DBUtils

def app():
    pg = PostgreSQL()

    db_version, conn = pg.get_connection()
    db_utils = DBUtils(conn)
    
    lista_animales = db_utils.get_animales();    
    

    pg.close_connection()