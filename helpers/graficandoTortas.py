import pandas as pd
import matplotlib.pyplot as plt

def graficarPromediosSalariales(dataframe, rangos, columnaInteresRango, columnaAPromediar, nombreGrafica):

    #1. Separo de graficas anteriores
    figura = plt.figure()

    #2. Calcular una nueva columna en e el data pot interes
    dataframe['rangoNuevo'] = pd.cut(dataframe[columnaInteresRango], bins = rangos)

    #Calcular la suma de los salarios por cada rango
    salarioPorRango = dataframe.groupby('rangoNuevo')[columnaAPromediar].sum()

    #4. Obtener los datos de salario y rango de edad
    salario = salarioPorRango.values
    rangoEdad = salarioPorRango.index

    #5. Creanis la torta
    plt.pie(salario, labels = rangoEdad, autopct = '%1.1f%%')
    plt.title("Distribucion de salarios")

    #6. graficar
    plt.savefig(f'./assets/img/{nombreGrafica}.png', dpi = 300, bbox_inches = 'tight')