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




fig, ax = crear_figura()
plotButton, clearButton, stopButton = crear_widgets(fig)
plt.show()