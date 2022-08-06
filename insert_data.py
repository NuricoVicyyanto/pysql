from connection import *

# memasukkan data pada tabel
sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = [("Vicky", "Bondowoso"),
       ("Cindy", "Bondowoso")]
# mycursor.execute(sql, val) # untuk insert satu data
mycursor.executemany(sql, val)  # untuk insert lebih dari satu data
mydb.commit()
# menghitung data yang berhasil diinput
print(mycursor.rowcount, "data inserted", mycursor.lastrowid)
