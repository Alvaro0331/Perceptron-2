import numpy as np

def train_perceptron(x,d):
    # Inicialización de pesos
    n_features = x.shape[1]
    bias=np.random.uniform(0,1)
    w=np.random.uniform(0,1, n_features)

    # Parámetros
    learning_rate = 0.01
    epoch=1
    historial = []  # Lista para almacenar el historial de pesos y bias
    # Entrenamiento del perceptrón
    while True:
        global_error=False
        #Calcular la salida del perceptrón para cada muestra
        for i in range(len(x)):
            #Calcular y
            v=np.dot(w, x[i]) + bias
            y= int(v >= 0)
            e=d[i]-y
            #Actualizar los pesos y el bias
            w=w+learning_rate*e*x[i]
            bias=bias+learning_rate*e
            #print(f"Epoch: {epoch}, Sample: {i}, Weights: {w}, Bias: {bias}, Error: {e}")
            if e !=0:
                global_error=True
        historial.append((epoch,w.copy(), bias))  # Almacenar el historial de pesos y bias
        if not global_error:
            #print(f"Entrenamiento completado en {epoch} epochs.")
            break
        if epoch >= 100:
            break
        epoch += 1
    print("\nPredicciones finales: ")
    for i in range(len(x)):
        v=np.dot(w, x[i]) + bias
        y= int(v >= 0)
        print(f"Input: {x[i]}, Output: {y}")
    correctos=0
    for i in range(len(x)):
        v=np.dot(w, x[i]) + bias
        y= int(v >= 0)
        if y == d[i]:
            correctos += 1
    print(f"Correctos: {correctos} de {len(x)}")
    return w, bias, historial