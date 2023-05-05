
class Materia:
    __dni = ""
    __nombre = ""
    __fecha = ""
    __nota = ""
    __aprobacion = ""

    def __init__(self, dni, nombre, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombre = nombre
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def getDNI (self):
        return self.__dni
    
    def getNombre (self):
        return self.__nombre
    
    def getFecha (self):
        return self.__fecha
    
    def getNota (self):
        return self.__nota
    
    def getAprobacion (self):
        return self.__aprobacion
    