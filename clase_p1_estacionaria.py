# INSTRUCCIONES PARA CORRER UN .py en Colab

# Escribir en una celda de código:

# ─── Instalación de Plotly 

# Se instala la librería Plotly para visualización interactiva (en caso de ser necesario)

#!pip install plotly

# ─── Ejecución del .py

# Subir el 'archivo.py' al entorno (desde el panel izquierdo)
# Correr

# %run clase_p1_estacionaria.py
# Descomentar la línea fig.show()


import numpy as np
import pandas as pd
import plotly.express as px

def poblacion_estacional_anual(P0, tasa_muertes, tasa_nacimientos, momento_nacimientos, delta_muestras):
  """
  PROPÓSITO: Devuelve un data frame con la evolución de la dinámica de una población durante un año. La misma comienza con *P0* individuos. Las muertes se producen  con una tasa *tasa_muertes* mensual y los nacimientos se producen de golpe en *momento_nacimientos*. La densidad de muestras que se toman por mes en el período de muertes es 1/*delta_muestras*.

  PRECONDICIONES:
    - Todos los parámetros deben ser positivos.
    - *momento_nacimientos* debe ser un entero del 1 al 12 indicando el mes.
  PARÁMETROS:
    - delta_muestras. Flotante. El intervalo temporal entre cada muestra.
  TIPO: DataFrame
  """
  meses = 12
  tasa_delta = tasa_muertes*delta_muestras
  muestras = np.arange(0, 12, delta_muestras) #star, stop, step
  poblacion = [P0]
   
  # identificar el momento en el arange
  i = 0
  while muestras[i]< momento_nacimientos:
    i+=1
  indice_nacimientos = i
   
  # calcular imagen de cada muestra hasta antes de los nacimientos
  for t in muestras[1:indice_nacimientos]:
    P0 = P0*(1 - tasa_delta)
    poblacion.append(P0)

  # Agregar los nacimientos al indice_nacimientos
  P0 = P0*(1+tasa_nacimientos)
  poblacion.append(P0)

  # continuar con los demás índices
  for t in muestras[indice_nacimientos + 1:]:
    P0 = P0*(1 - tasa_delta)
    poblacion.append(P0)

   #print(len(tiempo), len(poblacion))

  df = pd.DataFrame({'tiempo':muestras, 'poblacion': poblacion})
  return df


df = poblacion_estacional_anual(1000, 0.05, 1.5, 9, 0.2)

#print(df)

fig = px.scatter(df, x="tiempo", y="poblacion", title="Dinámica poblacional")

fig.update_traces(marker = {
  'size' : 10,
  'color' : 'red'
  }
)

# descomentar para ver el gráfico en colab
fig.show()

fig.write_html("clase_p1_estacionaria.html")
print("✅ Scatter generado: poblacion_estacional_anual.html")

#


