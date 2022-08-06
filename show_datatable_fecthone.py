from connection import *

# menampilkan hanya satu baris data saja
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchone()
print(myresult)