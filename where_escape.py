from connection import *

# %s untuk keluar dari query mencegah sql injection
sql = "SELECT * FROM users WHERE address = %s"
adr = ("Bondowoso", )

mycursor.execute(sql, adr)
myvalue = mycursor.fetchall()

for i in myvalue:
    print(i)
