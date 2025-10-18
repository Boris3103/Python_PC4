import sqlite3, csv

def solarizar_ventas():
    con = sqlite3.connect("base.db")
    cur = con.cursor()

    ventas = {}
    with open("ventas.csv", "r") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fecha = fila["fecha"]
            producto = fila["producto"]
            precio_usd = float(fila["precio"])
            
            cur.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (fecha,))
            tipo = cur.fetchone()
            if tipo:
                soles = precio_usd * tipo[0]
                ventas[producto] = ventas.get(producto, 0) + soles

    for producto, total in ventas.items():
        print(f"{producto}: S/ {total:.2f}")

    con.close()

solarizar_ventas()