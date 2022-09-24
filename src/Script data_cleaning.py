# %%
# pseudo codigo
# main()
#    datos = get_data(filename)
#    duplicados = remove_duplicates
#    fechas = cleaning_date (data)
#    save_data(reporte)

import os
import pandas as pd
from pathlib import Path
import numpy as np
from dateutil.parser import parse

root_dir = Path(".").resolve()

# %%
def get_data(filename):
    
    data_dir = 'raw'
    file_path = os.path.join(root_dir, "data", data_dir, filename)

    datos = pd.read_csv(file_path, encoding='latin-1', sep=';')
    print('get_data')
    print('La tabla contiene', datos.shape[0], 'filas', datos.shape[1], 'columnas')
    return datos

# %%
def remove_duplicates(datos):
  data = data.drop_duplicates() 
  data.reset_index(inplace=True, drop=True) 
  return data


# %%
def cleaning_date (data):

  fecha = '1985-12-03 00:00:00'
  pd.to_datetime(fecha,errors='coerce', format ='%Y/%m/%d')#no asignarle nada si se encuentra en ese formato 
  #y asignarle un formato de fecha para verificar si es una fecha correcta o es un NaT

  col='FECHA_INICIO_DESPLAZAMIENTO_MOVIL'
  data[col] = pd.to_datetime(data[col],errors='coerce') #cambiar el tipo de dato string a fecha
  data.info()

  #crear una funcion para intentar corregir las fechas incluyendo los nulos
  fechas = lambda x: parse(x)

  list_fechas = list() #convertir en una lista las fechas
  for fecha in data[col]:
    try: #intente hacerlo
        new_fecha = parse(fecha)
    except Exception as e:
        new_fecha = pd.to_datetime(fecha,errors='coerce')#me muestra los errores como NaT y no se detiene el codigo
       
    list_fechas.append(new_fecha)

  data['RECEPCION_CORREGIDA'] =list_fechas #crear una nueva columna con las fecha corregidas


# %%
def column_cleaning (data):

 col = 'UNIDAD'
 data [col].fillna('SIN_DATO', inplace=True)
 data [col].value_counts(dropna=False, normalize=True)

 col='EDAD'
 data[col].value_counts(dropna=False, normalize =True) 
 #verificar como vienen los datos de la columna de EDAD y nos damos cuenta que vienen algunos sin datos

 col='EDAD'
 data[col].replace({'SIN_DATO': np.nan}, inplace =True) #reemplaza las de SIN_DATE por nan sin numero asignado
 data[col]

 f = lambda x: x if pd.isna(x) else int(x) #definimos la funcion f para que si es nulo ponga x o si no ponga entero de f
 data[col] = data[col].apply(f)#para cambiar el tipo de dato de la columna EDAD de object a float



 def save_data(reporte, filename):
    # Guardar la tabla:

    out_name = 'resumen_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path)

# %%
def main():
    pass

if __name__ == "__main__":
    main()


