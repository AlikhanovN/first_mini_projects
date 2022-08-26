from peewee import *
import psycopg2
from pprint import pprint

connection = psycopg2.connect(
    dbname='startsql',
    user='alikhanov',
    password=f'12345',
    host='localhost'
)

cursor = connection.cursor()

request_call_table = '''CREATE TABLE request_call_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    phone_number VARCHAR(15),
    email VARCHAR(50),
    message TEXT
);'''
# Уже запущен и создан
# cursor.execute(request_call_table)
# connection.commit()
