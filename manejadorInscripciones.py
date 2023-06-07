from claseInscripcion import Inscripcion
import numpy as np
from numpy import ndarray
from clasePersona import Persona
import csv

class ManejadorInscripciones:
    __cantidad: int
    __incremento: int
    __inscripciones: ndarray
    __dimension: int
    
    def __init__(self, cantidad=0, incremento = 10, dimension = 10):
        self.__cantidad = cantidad
        self.__incremento = incremento
        self.__dimension = dimension
        self.__inscripciones = np.empty(self.__dimension, dtype = Inscripcion)

    def cargarInscripcion(self, MTC, MP):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
        else:
            print("Ingrese los datos de la persona a inscribir.")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            dni = input("Ingrese el DNI: ")
            unaPersona = Persona(nombre, direccion, dni)
            
            MTC.mostrarTalleres()
            ind = int(input("Ingrese el ID del taller a inscribirse: "))
            unTaller = MTC.getTaller(ind-1)
            MTC.actualizarVacante(ind-1)
            
            Fecha = str(input("Ingrese la fecha de inscripcion: "))
            unaInscripcion = Inscripcion(Fecha, unaPersona, unTaller)
            MP.cargarPersona(unaPersona)
            self.__inscripciones[self.__cantidad] = unaInscripcion
            self.__cantidad = self.__cantidad + 1
    
    def mostrarInscripcion(self):
        i = 0
        for ins in self.__inscripciones:
            print("\n {}:".format(i+1))
            print(ins)
            i = i + 1

    def buscarPorPersona(self, dni):
        bandera = False
        i = 0
        while i < self.__cantidad and not bandera:
            if self.__inscripciones[i].getDNI() == dni:
                bandera = True
            else: 
                i += 1
            return i
        
    def mostrarDatos(self):
        dni = input('Ingrese el DNI a consultar')
        ind = self.buscarPorPersona(dni)
        if ind == self.__cantidad:
            print('La persona no esta inscripta')
        else:
            print('Taller Inscripto: ' + self.__inscripciones[ind].getNombre())
            if self.__inscripciones[ind].getPago() == False:
                print('Monto que adeuda: {}'.format(self.__inscripciones[ind].getMontoInscripcion()))

    def mostrarPorTaller(self, MTC):
        MTC.mostrarTalleres()
        id = int(input('Ingrese un ID de Taller'))
        for i in range(self.__cantidad):
            if self.__inscripciones[i].getiD() == id:
                print(self.__inscripciones[i].getDatosInscripto())

    def registrarPago(self):
        dni = input('Ingrese el DNI a registrar el pago')
        ind = self.buscarPorPersona(dni)
        if ind == self.__cantidad:
            print('La persona no esta inscripta')
        else:
            self.__inscripciones[ind].actualizarPago()
            print('El pago se actualizo exitosamente')
            print("PAGO: {}" .format(self.__inscripciones[ind].getPago()))

    '''def guardar_inscripciones():
        headers = ['id', 'username', 'email']
        users = [
            ['1', 'user1', 'user1@pywombat.com'],
            ['2', 'user2', 'user2@pywombat.com'],
            ['3', 'user3', 'user3@pywombat.com'],
            ['4', 'user4', 'user3@pywombat.com'],
        ]

        with open('users.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow( headers) # Creamos las columnas

            for user in users:
                writer.writerow(user)'''


    def nuevoCSV(self):
        
        archivo = open("nuevoArchIns.csv", 'w')
        writer = csv.writer(archivo, delimiter = ';')
        for fila in range (self.__cantidad):
            lista = []
            self.__inscripciones[fila].crear(lista)
            print("Lista es: ", lista)
            
        for i in range(self.__cantidad):
            writer.writerow ([self.__inscripciones[i].getDNI(), str(self.__inscripciones[i].getiD()), str(self.__inscripciones[i].getFecha()), str(self.__inscripciones[i].getPago())])
        
        
        archivo.close()



