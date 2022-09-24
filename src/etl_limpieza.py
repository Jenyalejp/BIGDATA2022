
from sys import setprofile
from etl_reporte_llamadas import get_data,save_data
import pandas as pd


# main ()
# datos = leer_datos(nombre del archivo: str)- pd.dataframe
# datos = remover_duplicados_y_nulos (datos¨:pd.dataframe)--pd.dataframe
# datos = convertir_str_a_num(datos,col='edad') -- pd.dataframe
# datos = corregir_fechas(datos,col='fecha')--pd.dataframe
# save_data()

from fileinput import filename

def save_data(reporte, filename):
    # Guardar la tabla:

    out_name = 'resumen_' + filename
    out_path = os.path.join(root_dir, 'data', 'processed', out_name)
    reporte.to_csv(out_path)

save_data (reporte=datos,filename='llama****.cvs',step='clean')

out name = setprofile