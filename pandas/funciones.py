def promedio(archivo,columna):
    if columna in archivo:
        try:
            return archivo[columna].mean()
        except TypeError:
            print("La columna no es numérica.")
            return None
    else:
        print("La columna no existe en el DataFrame.")
        return None
    
