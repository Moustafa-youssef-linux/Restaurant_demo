import mysql.connector

dbconfig = { 'host': '127.0.0.1',
'user': 'rest',
'password': 'root123',
'database': 'restaurant', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
_SQL = """show tables"""
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

"""
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
values
('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""

cursor.execute(_SQL)

"""


"""
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
print(row)

"""
