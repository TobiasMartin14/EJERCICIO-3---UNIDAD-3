from manejadorTallerCapacitacion import ManejadorTallerCapacitacion
from manejadorInscripciones import ManejadorInscripciones
from manejadorPersonas import ManejadorPersonas
from menu import Menu



if __name__ == '__main__':
    MTC = ManejadorTallerCapacitacion()
    MI = ManejadorInscripciones()
    MP = ManejadorPersonas()
    M = Menu()
    M.opciones(MTC, MI, MP)
    