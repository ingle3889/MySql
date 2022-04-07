# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:36:32 2021

@author: Ramprasad Ingle

# this program use the parameterized query mysql using python. 
"""

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='India',
                                         user='root',
                                         password='123456')

    mySql_Create_Table_Query = """CREATE TABLE Employee ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             salary float NOT NULL,
                             birthday_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
    cursor = connection.cursor(prepared=True)
    # Parameterized query
    sql_insert_query = """ INSERT INTO Employee
                       (id, Name, salary, Joining_date) VALUES (%s,%s,%s,%s)"""
    # tuple to insert at placeholder
    tuple1 = (1, "Json",49000, "2019-03-23")
    tuple2 = (2, "Emma",39500, "2019-05-19")

    cursor.execute(sql_insert_query, tuple1)
    cursor.execute(sql_insert_query, tuple2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

