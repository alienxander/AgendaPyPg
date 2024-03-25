from app.utils.db_utils import PostgreSQL

def app():
    pg = PostgreSQL()

    conn = pg.get_connection()

    pg.close_connection()