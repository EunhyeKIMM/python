import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

name = input('검색할 이름:')
# cursor.execute("SELECT addr FROM tblAddr WHERE name = '김상형'")
query = f"SELECT addr FROM tblAddr WHERE name = '{name}'"
cursor.execute(query)

record = cursor.fetchone()

if record : print(f"{name}은 {record[0]}에 살고 있습니다.")
else : print(f"{name}은 없는 이름입니다.")

cursor.close()
con.close() 