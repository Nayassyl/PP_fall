import pymysql
connection = pymysql.connect(host="localhost", port=3306, user="root", password = "Qazzaq1@", database="test")
cursor = connection.cursor()
cursor.execute("select * from userss")
tables = cursor.fetchall()
print(tables[0][0])