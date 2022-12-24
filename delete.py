import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teste"
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (1,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros excluídos")