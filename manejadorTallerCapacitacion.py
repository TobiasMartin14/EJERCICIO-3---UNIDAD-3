import numpy as np
from numpy import ndarray
import csv
from claseTaller import Taller

class ManejadorTallerCapacitacion:
    __dimension: int
    __cantidad: int
    __talleres: ndarray
    __incremento: int
    
    def __init__(self, cantidad = 0, incremento = 5):
        self.__cantidad = cantidad
        self.__incremento = incremento
        
    def cargarTalleres(self):
        bandera = False
        archivo = open('Talleres.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if bandera == False:
                cantidad = fila[0]
                bandera = True
                cantidad = int(fila[0])
                self.__talleres = np.empty(cantidad, dtype = Taller)
            else:
                self.__talleres[self.__cantidad] = Taller(int(fila[0]), fila[1], int(fila[2]), float(fila[3]))
                self.__cantidad += 1

    def mostrarCarga(self):
        for talleres in self.__talleres:
            print(talleres)
        
    def mostrarTalleres(self):
        for i in range(self.__cantidad):
            print('{}) Nombre: {} '.format((i+1), self.__talleres[i].getNombre()))
    
    def getTaller(self, ind):
        return self.__talleres[ind]

    def actualizarVacante(self, ind):
        self.__talleres[ind].actualizarVacantes()