import numpy as np

def mejor_precio(tabla):
    lowest_sum = np.sum(a.T[1, 1:])
    lowest_index = 1
    for column in a.T[1:]:
        if np.sum(column) < lowest_sum:
            lowest_sum = np.sum(column)
            lowest_index = np.sum()
    return lowest_index, lowest_sum

destinos = ["Ixtapa", "Acapulco", "Cancún"]

a = np.array([[1500, 3000, 4500], 
              [800, 1200, 100], 
              [500, 800, 1200], 
              [ 120, 240, 360]])

lowest_index, lowest_sum = mejor_precio(a)
print("El mejor precio es {} por {}".format(destinos[lowest_index], lowest_sum))