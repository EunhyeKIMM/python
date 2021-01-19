import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")

table = cursor.fetchall()
# for record in table:
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

for name, phone, addr in table:
    print(f"이름: {name}, 전화: {phone}, 주소: {addr}")

cursor.close()
con.close() 