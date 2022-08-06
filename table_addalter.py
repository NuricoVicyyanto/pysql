from connection import *

# menambahkan kolom bari pada tabel yang sudah tersedia
mycursor.execute(
    "ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
