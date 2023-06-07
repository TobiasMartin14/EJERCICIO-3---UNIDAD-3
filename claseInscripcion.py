

class Inscripcion:
    __fechaInscripcion = str
    __pago = bool
    __persona = object
    __taller = object

    def __init__(self, fecha, pers, tall, pago = False):
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__persona = pers
        self.__taller = tall

    def __str__(self):
        return 'Inscripcion: ' + '\n' + 'Fecha de Inscripcion: ' + self.__fechaInscripcion + '\n' + 'Pago: ' + str(self.__pago) + '\n' + 'Persona: ' + str(self.__persona) + '\n'
    
    def getFecha(self):
        return self.__fechaInscripcion
    
    def getPago(self):
        return self.__pago
    
    def getDNI(self):
        return self.__persona.getDNI()
    def getNombre(self):
        return self.__persona.getNombre()
    def getMontoInscripcion(self):
        return self.__taller.getMontoInscripcion()
    def getiD(self):
        return self.__taller.getiD()
    def getDatosInscripto(self):
        return 'Nombre: ' + str(self.__persona.getNombre()) + ' ' + 'Direccion: ' + str(self.__persona.getDireccion()) + ' ' + 'DNI: ' + str(self.__persona.getDNI())
    def actualizarPago(self):
        self.__pago = True

    def crear (self, lista):
        fila = [self.__persona.getDNI(), self.__taller.getiD(), self.__fechaInscripcion, self.__pago]
        lista.append(fila)