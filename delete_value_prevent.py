from connection import *

sql = "DELETE FROM users WHERE name = %s"
val = ("monyet", )
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "data dihapus")
