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

# obtenemos todos los datos de la tabla data
cursor_data = mydb.cursor()
cursor = mydb.cursor()
sql = "SELECT * FROM data"
cursor_data.execute(sql)
results_data = cursor_data.fetchall()

# creamos la tabla companies (si no existe)
create = """CREATE TABLE IF NOT EXISTS companies (
    id VARCHAR(40) NOT NULL UNIQUE,
    company_name VARCHAR(24) NOT NULL,
    PRIMARY KEY(id))
    """
cursor.execute(create)

# creamos tabla charges (si no existe)
create = """CREATE TABLE IF NOT EXISTS charges (
    id VARCHAR(40) NOT NULL UNIQUE,
    company_id VARCHAR(40) NOT NULL,
    amount VARCHAR(22) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at VARCHAR(19) NOT NULL,
    paid_at VARCHAR(10) NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies (id))"""
cursor.execute(create)

# llenar tabla companies
for i in results_data:
    insert = "INSERT INTO `companies` (`id`, `company_name`) VALUES (%s, %s)"
    values = (i[2], i[1])
    try:
        cursor.execute(insert, values)
    except:
        print("Ya existe en companies")
    pass

mydb.commit()

# llenar tabla charges
for i in results_data:
    insert = "INSERT INTO `charges` (`id`, `company_id`, `amount`, `status`, `created_at`, `paid_at`) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (i[0], i[2], i[3], i[4], i[5], i[6])
    try:
        cursor.execute(insert, values)
    except:
        print("Error al subir en tabla charges")
        

mydb.commit()
