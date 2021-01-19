import MySQLdb

db = MySQLdb.connect(db="employees", host="localhost", user="iot", passwd="1234")
c = db.cursor()

query = "select * from departments" 
c.execute(query)

rows = c.fetchall()
for no, name in rows:
    print(f'{no}, {name}')

c.close()
db.close() 