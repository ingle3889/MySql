# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:36:32 2021

@author: Ramprasad Ingle

# this program selects entries from table. 
"""

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='India',
                                         user='root',
                                         password='123456')

    select_Query = "select * from Employee"
    cursor = connection.cursor()
    cursor.execute(select_Query)
    
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("salary  = ", row[2])
        print("birthday_date= ", row[3], "\n")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

