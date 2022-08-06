from connection import *

# menampilkan data dari tabel dengan batasan tertentu
sql = "SELECT * FROM users LIMIT 1"
mycursor.execute(sql)
myvalue = mycursor.fetchall()

for i in myvalue:
    print(i)
