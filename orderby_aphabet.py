from connection import *

# mengurutkan sesuai alphabet a-z
sql = "SELECT * FROM users ORDER BY name"
mycursor.execute(sql)
myvalue = mycursor.fetchall()

for i in myvalue:
    print(i)
