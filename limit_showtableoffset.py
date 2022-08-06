from connection import *

# membatasi jumlah data yang ditampilkan dengan limit
# offset berfungsi untuk menentukan data awal yang akan mulai ditampilkan
sql = "SELECT * FROM users LIMIT 1 OFFSET 1"
mycursor.execute(sql)

myvalue = mycursor.fetchall()

for i in myvalue:
    print(i)