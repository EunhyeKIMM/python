import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")

while True:
    record = cursor.fetchone()
    if record == None: break

    print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

cursor.close()
con.close() 