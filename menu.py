
class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, MTC, MI, MP):
        indice = True
        while indice:
            print("\n") 
            print ("Opcion 1: Cargar los datos de los talleres en la clase TallerCapacitacion.")
            print ("Opcion 2: Inscribir una persona en un taller.")
            print ("Opcion 3: Consultar inscripción.")
            print ("Opcion 4: Consultar inscriptos.")
            print ("Opcion 5: Registrar pago.")
            print ("Opcion 6: Guardar inscripciones.")
            print ("Opcion 7: Salir.")
            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                MTC.cargarTalleres()
                MTC.mostrarCarga()
            elif (self.__opcion == 2):
                MI.cargarInscripcion(MTC, MP)
                MI.mostrarInscripcion()
            elif (self.__opcion == 3):
                MI.mostrarDatos()
            elif (self.__opcion == 4):
                print("INSCRIPTOS:")
                MI.mostrarPorTaller(MTC)
            elif (self.__opcion == 5):
                MI.registrarPago()
            elif (self.__opcion == 6):
                #MI.guardarInscripciones()
                MI.nuevoCSV()
            elif (self.__opcion == 7):
                indice = False
            else:
                print("La opcion ingresada no es valida.")