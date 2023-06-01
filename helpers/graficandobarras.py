import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataframe, columnaX, columnaY, nombreGrafica):
    
    #1. Definir una lissta con colores
    colores = ['green', 'blue', 'red']

    #2. Obtener el promedio de los salarios
    salarioPromedio = dataframe.groupby(columnaX)[columnaY].mean()

    #3. Comienzo a generar la grafica de barras
    plt.bar(salarioPromedio.index, salarioPromedio, color = colores)
    plt.xlabel("Cargo")
    plt.xlabel("Salario Promedio")
    plt.title("Salario promedio por cargo")

    #4. Guardamos la grafica
    plt.savefig(f'./assets/img/{nombreGrafica}.png', dpi = 300, bbox_inches = 'tight')