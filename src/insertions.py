from  mysql.connector import Error
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        db='mysql_python_conection'
    )
    if connection.is_connected():
        print("Ok!")
except Error as ex:
    print("Error during connection: {}".format(ex))
finally:
    if connection.is_connected():
        connection.close()
        print("Conection closed.")