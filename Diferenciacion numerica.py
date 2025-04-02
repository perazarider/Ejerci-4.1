import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = sin(x)
def f(x):
    return np.sin(x)

# Derivada analítica de f(x) = sin(x), que es cos(x)
def df_analytical(x):
    return np.cos(x)

# Método de diferencias finitas hacia adelante
def forward_diff(f, x, h=0.1):
    return (f(x + h) - f(x)) / h

# Método de diferencias finitas hacia atrás
def backward_diff(f, x, h=0.1):
    return (f(x) - f(x - h)) / h

# Método de diferencias finitas centradas
def central_diff(f, x, h=0.1):
    return (f(x + h) - f(x - h)) / (2*h)

# Definir intervalo de evaluación [0, π] con un paso de h = 0.1
a, b = 0, np.pi
h = 0.1
x_vals = np.arange(a, b, h)  # Se utiliza arange para mantener el paso h

# Cálculo de la derivada analítica
df_exact = df_analytical(x_vals)

# Aproximaciones numéricas
df_forward = forward_diff(f, x_vals, h)
df_backward = backward_diff(f, x_vals, h)
df_central = central_diff(f, x_vals, h)

# Errores absolutos
error_forward = np.abs(df_forward - df_exact)
error_backward = np.abs(df_backward - df_exact)
error_central = np.abs(df_central - df_exact)

# Gráfica de la función y sus derivadas
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f(x_vals), '-', label='f(x) = sin(x)')
plt.plot(x_vals, df_exact, 'k-', label="Derivada Analítica (cos(x))")
plt.plot(x_vals, df_forward, 'r--', label="Diferencias Hacia Adelante")
plt.plot(x_vals, df_backward, 'g-.', label="Diferencias Hacia Atrás")
plt.plot(x_vals, df_central, 'b:', label="Diferencias Centradas")
plt.xlabel('x')
plt.ylabel("Derivada")
plt.legend()
plt.title("Comparación de Métodos de Diferenciación Numérica")
plt.grid()
plt.show()

# Gráfica de los errores
plt.figure(figsize=(10, 6))
plt.plot(x_vals, error_forward, 'r--', label="Error Hacia Adelante")
plt.plot(x_vals, error_backward, 'g-.', label="Error Hacia Atrás")
plt.plot(x_vals, error_central, 'b:', label="Error Centrado")
plt.xlabel('x')
plt.ylabel("Error absoluto")
plt.legend()
plt.title("Errores en Diferenciación Numérica")
plt.grid()
plt.show()

# Crear tabla de resultados
import pandas as pd

data = {
    'x': x_vals,
    'Derivada Analítica': df_exact,
    'Diferencias Adelante': df_forward,
    'Error Adelante': error_forward,
    'Diferencias Atrás': df_backward,
    'Error Atrás': error_backward,
    'Diferencias Centradas': df_central,
    'Error Centrado': error_central
}

df_results = pd.DataFrame(data)
df_results.head(10)  # Mostrar primeras 10 filas de la tabla