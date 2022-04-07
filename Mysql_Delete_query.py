# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:36:32 2021

@author: Ramprasad Ingle

# this program Deletes entry from table in Mysql. 
"""

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='India',
                                         user='root',
                                         password='123456')

    cursor = connection.cursor()
    print("Laptop table before deleting a row")
    sql_select_query = """select * from Employee where id = 7"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Delete a record
    sql_Delete_query = """Delete from Employee where id = 7"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)

    # Verify using select query (optional)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

