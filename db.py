import mysql.connector
import os

def get_connection():

    return mysql.connector.connect(

        host=os.environ.get("MYSQLHOST", "localhost"),

        user=os.environ.get("MYSQLUSER", "root"),

        password=os.environ.get("MYSQLPASSWORD", ""),

        database=os.environ.get("MYSQLDATABASE", "sentiment_db"),

        port=int(os.environ.get("MYSQLPORT", 3306))

    )