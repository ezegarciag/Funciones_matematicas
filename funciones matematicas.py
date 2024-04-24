import numpy as np
import plotly.graph_objects as go

def plot_function_3d(func, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)
    
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
    fig.update_layout(title="Gráfico 3D de la función",
                      scene=dict(
                          xaxis_title='X',
                          yaxis_title='Y',
                          zaxis_title='Z'
                      ))
    fig.show()

# Función para evaluar una función ingresada por el usuario
def evaluar_funcion_3d(func_str):
    def func(x, y):
        return eval(func_str)
    return func

# Pide al usuario ingresar una función
func_str_3d = input("Ingrese la función en términos de 'x' e 'y': ")

# Evalúa la función
func_3d = evaluar_funcion_3d(func_str_3d)

# Define el rango en el que deseas graficar la función
x_range_3d = (-10, 10)
y_range_3d = (-10, 10)

# Graficación 3D
plot_function_3d(func_3d, x_range_3d, y_range_3d)
