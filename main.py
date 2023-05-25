import pandas as pd
from data.data1 import apartamento1, apartamento2
from helpers.crearTablasHTML import crearTabla
#from data.data1 import apartamento2

tabla1 = pd.DataFrame(apartamento1, columns = ['Edad'])
tabla2 = pd.DataFrame(apartamento2, columns = ['Edad'])
tabla3 = pd.read_csv("./data/empleados.csv")

#Filtrado o aplicando condiciones a mi dataframe
#1. Orientada a la logica de consultas (Query's)
#empleadosJovenes1 = tabla3.query('edad<28 and cargo=="analista1"')
##print(empleadosJovenes1)

#2. Orientada al dataframe
#empleadosJovenes2 = tabla3[(tabla3['edad']<28) & (tabla3['cargo']=="analista1")]
##print(empleadosJovenes2)

#Creando la tabla
#crearTabla(empleadosJovenes1, "tabla")

analistas1 = tabla3.query('cargo=="analista1"')

analistas2 = tabla3.query('cargo=="analistas2"')

jubilados = tabla3.query('edad>=50')