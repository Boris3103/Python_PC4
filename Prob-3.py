def contar_lineas_codigo(ruta):
    try:
        if not ruta.endswith(".py"):
            print("El archivo debe tener extensión .py")
            return
        
        with open(ruta, "r") as f:
            lineas = f.readlines()
        
        codigo = [l for l in lineas if l.strip() and not l.strip().startswith("#")]
        print(f"Número de líneas de código: {len(codigo)}")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error:", e)

contar_lineas_codigo("hello.py")
