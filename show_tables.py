from connection import *

# menampilkan tabel yang tersedia
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
