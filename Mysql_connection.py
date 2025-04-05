import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(mydb)



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor=conn.cursor()
cursor.execute("select * from DataRevature.student")
for row in cursor:
    print(row)