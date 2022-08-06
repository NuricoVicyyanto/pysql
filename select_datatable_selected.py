from connection import *

# menampilkan sebagian isi kolom saja
mycursor.execute("SELECT name, address FROM users")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
