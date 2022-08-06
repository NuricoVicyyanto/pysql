from connection import *

# menghapus nilai dalam tabel menggunakan nama
sql = "DELETE FROM users WHERE name = 'singa'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "data dihapus")
