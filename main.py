import config
import mysql.connector
from mysql.connector import errorcode


# create database and user

def get_conn():

    try:
        conn = mysql.connector.connect(
            user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST
        )

        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return 0
        else:
            return err


conn = get_conn()

if conn == 0:
    print("acceso denegado")
elif isinstance(conn, mysql.connector.Error):
    print("otro error")
else:
    cursor = conn.cursor()
    for line in open("schema.sql"):
        cursor.execute(line)
# aplicar esquema de freeradius y daloradius
    
conn.close()


#modificar mods-available
#dialect = "mysql"
#comentar driver de arriba
#driver = "rlm_sql_${dialect}"
#server, port, login, password, radius_db = "radiusdb"
#comentar tls mysql
#descomentar read_clints = yes

