
class Taller:
    __idTaller = int
    __nombre = str
    __vacantes = int
    __montoInscripcion = float
    __inscripciones = list

    def __init__(self, id, nom, vac, mon):
        self.__idTaller = id 
        self.__nombre = nom
        self.__vacantes = vac
        self.__montoInscripcion = mon
        self.__inscripciones = []


    def getiD(self):
        return self.__idTaller
    def getNombre(self):
        return self.__nombre
    def getVacantes(self):
        return self.__vacantes
    def getMontoInscripcion(self):
        return self.__montoInscripcion
    def getInscripciones(self):
        return self.__inscripciones
    def __str__(self):
        return str(self.__idTaller) + ' ' + self.__nombre + ' ' + str(self.__vacantes) + ' ' + str(self.__montoInscripcion)
    def actualizarVacantes(self):
        self.__vacantes = self.__vacantes - 1