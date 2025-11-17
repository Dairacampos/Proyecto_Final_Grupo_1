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
    

def percentiles(archivo, nombre_columna):
    try:
        df = pd.read_csv(archivo)
        if nombre_columna not in df.columns:
            return 'Error al procesar la columna'
        
        est = df[nombre_columna].describe()
        return f"Percentil 25: {est['25%']}, Percentil 50: {est['50%']}, Percentil 75: {est['75%']}"
    
    except FileNotFoundError:
        return 'Error al procesar la columna'
    except Exception as e:
        return 'Error al procesar la columna'