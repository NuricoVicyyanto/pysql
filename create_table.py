from connection import *

# membuat tabel pada database
mycursor.execute(
    "CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")
