from connection import *

sql = "UPDATE users SET name = 'monyet' WHERE name = 'macan' "
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "data diubah")
