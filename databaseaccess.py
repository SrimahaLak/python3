import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="admin",database="fan")  #no need to write connection name

obj=db.cursor()
obj.execute("select * from laptop;")
result = obj.fetchall()

for i in result:
    print(i)