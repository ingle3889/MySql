# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:36:32 2021

@author: Ramprasad Ingle

# this program creates table in Mysql. 
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

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Employee Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

