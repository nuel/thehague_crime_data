# Create database schema
import sqlite3

conn = sqlite3.connect('data/delicts.db')

c = conn.cursor()
c.execute('create table delicts (delict smallint, latitude varchar(20), longitude varchar(20), month smallint, year smallint, count smallint, name varchar(100), neighbourhood int, district int)')

conn.commit()
c.close()
