import requests, sqlite3

def guardar_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?year=2023"
    datos = requests.get(url).json()

    con = sqlite3.connect("base.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sunat_info (fecha TEXT, compra REAL, venta REAL)")
    
    for d in datos:
        cur.execute("INSERT INTO sunat_info VALUES (?, ?, ?)", 
                    (d['fecha'], d['compra'], d['venta']))
    
    con.commit()
    for row in cur.execute("SELECT * FROM sunat_info LIMIT 5"):
        print(row)
    con.close()

guardar_tipo_cambio()