import mysql.connector
from mysql.connector.errors import Error

def get_connection():
    connection = mysql.connector.connect(
            host = 'database-1.ckgggmo40ahf.us-east-2.rds.amazonaws.com',
            database = 'streamlit_db',
            user = 'python_user',
            password='2105'
    )
    return connection
