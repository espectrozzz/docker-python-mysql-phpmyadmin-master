# coding: utf-8

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="databasename",
  port=3320,
  user="root",
  password="123"
)

print(mydb)