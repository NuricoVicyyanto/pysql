import mysql.connector

# menghubungkan autentikasi database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mysql_py"  # ditambahkan untuk mengakses ke spesifik database
)

# cek koneksi database
if mydb.is_connected():
    print("database connect")

# inisiasi cursor
mycursor = mydb.cursor()
