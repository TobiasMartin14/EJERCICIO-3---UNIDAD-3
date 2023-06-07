
class Persona:
    __nombre = str
    __direccion = str
    __dni = str

    def __init__(self, no, di, dn):
        self.__nombre = no
        self.__direccion = di
        self.__dni = dn
    
    def __str__(self):
        return self.__nombre + ' ' + self.__direccion + ' ' + self.__dni
    
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getDNI(self):
        return self.__dni
    
    def __str__(self):
        return '\n' + 'Nombre: ' + self.__nombre + '\n' + 'Direccion: ' + self.__direccion + '\n' + 'DNI: ' + self.__dni    
    