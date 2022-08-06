from connection import *

sql = "SELECT * FROM users WHERE name = 'vicky' "
mycursor.execute(sql)
myresult = mycursor.fetchall()

for i in (myresult):
    print(i)
