def promedios(archivo, nombre_columna):
    try:
        df = pd.read_csv(archivo)
        if nombre_columna in df.columns:
            return df[nombre_columna].mean()
        else:
            print("Error al procesar la columna.")
            return None
    except Exception as e:
        print("Error al procesar la columna")
        return None
    
