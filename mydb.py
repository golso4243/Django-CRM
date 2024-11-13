
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=os.getenv('DB_PASSWORD'),
)

# Prepare a cursor object using cursor() method
cursor = dataBase.cursor()

# Create database dcrm
cursor.execute('CREATE DATABASE dcrm')

print('Database dcrm created successfully')
