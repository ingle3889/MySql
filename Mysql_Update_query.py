# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:36:32 2021

@author: Ramprasad Ingle

# this program upadtes entry in table . 
"""

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='India',
                                         user='root',
                                         password='123456')

    cursor = connection.cursor()

    print("Before updating a record ")
    select_query = """select * from Employee where id = 1"""
    cursor.execute(select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    update_query = """Update Employee set Price = 7000 where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

