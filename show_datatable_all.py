from connection import *

# menampilkan seluruh data pada tabel
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
