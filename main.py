import pandas as pd
from data.data1 import apartamento1, apartamento2
from helpers.graficandoTortas import graficarPromediosSalariales
from helpers.graficandobarras import graficarPromedioSalarial
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

analistas2 = tabla3.query('cargo=="analista2"')

jubilados = tabla3.query('edad>=50')

#Generamos tablas
crearTabla(analistas1, "analistas1")
crearTabla(analistas2, "analistas2")
crearTabla(jubilados, "jubilados")

#Generamos graficas
graficarPromedioSalarial(jubilados, 'cargo', 'salario', 'promedioJubilados')
graficarPromediosSalariales(analistas1, [20, 30, 40, 50, 60], 'edad', 'salario', 'promediosAnalistas1')