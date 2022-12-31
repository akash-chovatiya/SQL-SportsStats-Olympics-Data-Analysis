"""to run it ctrl+B"""

import mysql
import mysql.connector
import pandas as pd
from datetime import datetime

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="akash_sql",
	database="sports"
	)

mycursor = db.cursor()
sports = pd.read_csv(r"E:\LEARNING__Courses__Deep Learning\SQL__MySQL__NoSQL\Coursera_SQL Project\SportsStats\athlete_events.csv")
sports=sports.fillna(0)
#print(sports)

#mycursor.execute("use database_name")
#mycursor.execute("create database sports")
#mycursor.execute("drop database akkiabc")
#mycursor.execute("show databases")
#mycursor.execute("show tables")
#mycursor.execute("Describe athlete_events")

#for x in mycursor:
#	print(x)

if db.is_connected():
	mycursor = db.cursor()
	mycursor.execute("select database();")
	record = mycursor.fetchone()
	print("You're connected to database: ", record)
	mycursor.execute("DROP TABLE IF EXISTS Athlete_events;")
	print('Creating table....')
	mycursor.execute("Create Table Athlete_events (ID int NOT NULL, Name varchar(255) NOT NULL, sex varchar(20) NOT NULL, Age int NOT NULL, Height float(5,1) NOT NULL, Weight float(5,1) NOT NULL, Team varchar(255) NOT NULL, NOC varchar(50) NOT NULL, Games varchar(50) NOT NULL, Year int(4) NOT NULL, Season varchar(6) NOT NULL, City varchar(50) NOT NULL, Sport varchar(50) NOT NULL, Event varchar(255) NOT NULL, Medal varchar(10) NOT NULL)")
	print("Table is created....")
	for i,row in sports.iterrows():
		sql = "INSERT INTO sports.athlete_events VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		mycursor.execute(sql, tuple(row))
		print("Record inserted")
		# the connection is not auto committed by default, so we must commit to save our changes
		db.commit()