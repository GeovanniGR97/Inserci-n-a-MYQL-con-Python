from faker import Faker
from mysql.connector import Error
import mysql.connector

fake = Faker()
data = []

# Generar datos simulados
for _ in range(100):
    data.append((
        fake.uuid4(),  # UUID que no se usará en la inserción
        fake.name(),  # Nombre
        fake.random_int(min=1000, max=1000000),  # Población simulada
        fake.random_number(digits=4)  # Kilómetros simulados
    ))

# Preparar los datos excluyendo el UUID
prepared_data = [(name, population, kilometers) for _, name, population, kilometers in data]

try:
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        db='undostres'
    )
    if connection.is_connected():
        cursor = connection.cursor()

        # Ejecutar la inserción
        cursor.executemany("""INSERT INTO ciudad (name, population, kilometers)
                              VALUES (%s, %s, %s)""", prepared_data)
        
        if len(prepared_data) == cursor.rowcount:
            connection.commit()
            print("{} rows inserted.".format(len(prepared_data)))
        else:
            connection.rollback()

except Error as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed.")
