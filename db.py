import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # Change this if your MySQL has a password
        database="sentiment_db"
    )