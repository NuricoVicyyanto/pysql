from connection import *

# mengurutkan sesuai alphabet dari z-a
sql = "SELECT * FROM users ORDER BY name DESC"
mycursor.execute(sql)
myvalue = mycursor.fetchall()

for i in myvalue:
    print(i)
