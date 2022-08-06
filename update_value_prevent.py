from connection import *

sql = "UPDATE users SET name = %s WHERE name = %s"
val = ("koala", "monyet")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "data diupdate")