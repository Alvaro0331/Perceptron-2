import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

# Creacion de la figura
def crear_figura():
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes([0.1, 0.1, 0.6, 0.8]) # [left, bottom, width, height]
    ax.set_title("Práctica 2")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlabel("X2", fontsize=12)
    ax.set_ylabel("X1", fontsize=12)
    #Dibujo de ejes
    ax.axhline(y=0, color='black', linewidth=0.7)
    ax.axvline(x=0, color='black', linewidth=0.7)
    
    """ #Leyenda
    leyenda = [
        plt.Line2D([0], [0], marker='o', color='w', label='Clase 0', markerfacecolor='blue', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', label='Clase 1', markerfacecolor='red', markersize=8),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=8, label='Sin clasificar'),
        plt.Line2D([0], [0], linestyle='--', color='green', label='Frontera'),
    ]
    ax.legend(handles=leyenda, loc='upper right', fontsize=8) """
    return fig, ax

#Creacion de los widgets
def crear_widgets(fig):
    # Botones
    plotButton=widgets.Button(plt.axes([0.75, 0.3, 0.1, 0.15]), 'Plot', color='lightblue', hovercolor='skyblue')
    stopButton=widgets.Button(plt.axes([0.75, 0.2, 0.1, 0.05]), 'Stop', color='lightyellow', hovercolor='yellow')
    clearButton=widgets.Button(plt.axes([0.75, 0.1, 0.1, 0.05]), 'Clear', color='lightcoral', hovercolor='salmon')
    
    return plotButton, clearButton, stopButton

#Evento para agregar puntos con el mouse
puntos = []  # Lista para almacenar los puntos clickeados
markers = [] # Lista para almacenar los objetos de los puntos dibujados
lineas = [] # Lista para almacenar la línea dibujada
def onclick(event):
    if event.inaxes == ax:
        x, y = event.xdata, event.ydata
        marker, = ax.plot(x, y, 'ko')  # Dibuja un punto negro en la posición clickeada
        puntos.append((x, y))  # Agrega el punto a la lista de puntos
        markers.append(marker)  # Agrega el objeto del punto a la lista de markers
        fig.canvas.draw()  # Actualiza la figura para mostrar el nuevo punto


#Evento para limpiar los puntos
def clear(event):
    for marker in markers:
        marker.remove()  # Elimina el punto de la figura
    markers.clear()  # Reinicia la lista de markers
    puntos.clear() # Reinicia la lista de puntos
    clear_line()  # Limpia la línea de decisión

#Funcion para limpiar la linea
def clear_line():
    for linea in lineas:
        linea.remove()  # Elimina la línea de la figura
    lineas.clear()  # Reinicia la lista de líneas
    fig.canvas.draw()  # Actualiza la figura para reflejar los cambios

fig, ax = crear_figura()
plotButton, clearButton, stopButton = crear_widgets(fig)
fig.canvas.mpl_connect('button_press_event', onclick)
clearButton.on_clicked(clear)
plt.show()