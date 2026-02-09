'''import mysql.connector
import logging

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',   
            user='root',
            password='',        
            database='test'
        )
        logging.info("Successfully connected to the database.")
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to the database: {err}")
        return None
   '''
