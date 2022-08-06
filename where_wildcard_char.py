from connection import *


sql = "SELECT * FROM users WHERE address LIKE '%ndo%'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in (myresult):
    print(i)