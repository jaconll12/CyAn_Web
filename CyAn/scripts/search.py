import mysql.connector
from mysql.connector import Error
import sys
import json

tar = sys.argv[1]
tar = str(tar)
print (tar)


with open('../db.json') as json_data:
        d = json.load(json_data)
        for p in d['db']:
            datab = p["database"]
            host = p["host"]
            user = p["user"]
            password = p["password"] 
try:
    connection = mysql.connector.connect(host=host,
                                         database=datab,
                                         user=user,
                                         password=password,
                                         auth_plugin='mysql_native_password')

    #sql_select_Query = "SELECT * from findings WHERE url = "+ str(tar)
    
    #cursor.execute(sql_select_Query)
    cursor = connection.cursor(buffered=True)
    sql_select_query = """select * from findings where url = %s"""
    cursor.execute(sql_select_query, (tar,))
    #cursor = connection.cursor()

    record = cursor.fetchall()

    for row in record:
        print("Date Ran = ", row[0], )
        print("URL = ", row[1])
        print("Nikto Results = ", row[2])
        print("Nikto Results = ", row[3])
        print("Zap Results  = ", row[4], "\n")


except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")