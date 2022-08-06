from django.db import connection
from matplotlib.pyplot import connect


from connection import *

# menampilkan database
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
