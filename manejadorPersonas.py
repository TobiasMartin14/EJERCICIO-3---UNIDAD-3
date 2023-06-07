from clasePersona import Persona

class ManejadorPersonas:
    __listaP = []

    def __init___(self):
        self.__listaP = []

    def cargarPersona(self, unaPersona):
        self.__listaP.append(unaPersona)

    