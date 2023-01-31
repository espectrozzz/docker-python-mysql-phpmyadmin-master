import mysql.connector
import pandas as pd

# conexión a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  database="databasename",
  port=3320,
  user="root",
  password="123"
)

# obtener datos a exportar
cursor = mydb.cursor()
sql = "SELECT * FROM data"
cursor.execute(sql)
results = cursor.fetchall()

# crear DataFrame y prepararlo para su exportación
data = pd.DataFrame(results, columns=['id', 'name', 'company_id', 'amount', 'status', 'created_at', 'paid_at'])

# exportar a csv
data.to_csv("extact.csv")
