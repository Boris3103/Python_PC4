def procesar_temperaturas():
    try:
        with open("temperaturas.txt", "r") as f:
            datos = [line.strip().split(",") for line in f if line.strip()]
        
        temperaturas = [float(temp) for _, temp in datos]
        promedio = sum(temperaturas) / len(temperaturas)
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)

        with open("resumen_temperaturas.txt", "w") as f:
            f.write(f"Promedio: {promedio:.2f}\n")
            f.write(f"Máxima: {max_temp:.2f}\n")
            f.write(f"Mínima: {min_temp:.2f}\n")
        print("Archivo resumen generado correctamente.")

    except FileNotFoundError:
        print("El archivo temperaturas.txt no existe.")
    except Exception as e:
        print("Error:", e)

procesar_temperaturas()