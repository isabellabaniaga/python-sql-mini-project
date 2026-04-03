import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio INTEGER)")

cursor.execute("INSERT INTO productos VALUES ('Laptop', 800)")
cursor.execute("INSERT INTO productos VALUES ('Mouse', 25)")

conexion.commit()

print("Todos los productos:")
cursor.execute("SELECT * FROM productos")
datos = cursor.fetchall()

for dato in datos:
    print(dato)

print("\nProductos con precio mayor a 100:")
cursor.execute("SELECT * FROM productos WHERE precio > 100")
datos = cursor.fetchall()

for dato in datos:
    print(dato)

conexion.close()