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
    
def desviacion(archivo, columna):
    try:
        ds = pd.read_csv(archivo)
        if columna not in ds.columns:
            return "Error al procesar la columna"
        return ds[columna].std()
    except FileNotFoundError:
        return "Error al procesar la columna"
    except Exception as e:
        return f"Error al procesar la columna"