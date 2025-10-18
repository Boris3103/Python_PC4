def crear_tabla(n):
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")

def leer_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No existe ese archivo de tabla.")

def leer_linea_tabla(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            print(lineas[m-1].strip())
    except FileNotFoundError:
        print("No existe ese archivo de tabla.")
    except IndexError:
        print("La línea indicada no existe.")
        