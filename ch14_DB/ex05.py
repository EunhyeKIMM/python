import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name = input("이름: ")
phone = input("전화번호: ")
addr = input("주소: ")

query = f"INSERT INTO tblAddr VALUES('{name}', '{phone}', '{addr}')"
cursor.execute(query)

con.commit()

cursor.close()
con.close()