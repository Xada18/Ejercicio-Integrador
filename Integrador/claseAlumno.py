
class Alumno:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __año = ""

    def __init__(self, dni, apellido, nombre, carrera, año):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__año = año

    def __str__(self):
        return f"{self.__año}° año, {self.__apellido}, {self.__nombre}, {self.__dni},  {self.__carrera}, "

    def getDNI (self):
        return self.__dni
    
    def getApellido (self):
        return self.__apellido
    
    def getNombre (self):
        return self.__nombre
    
    def getCarrera(self):
        return self.__carrera
    
    def getAño (self):
        return self.__año
    
    def getAyN(self):
        return f"{self.__apellido}, {self.__nombre}"
      
    def __lt__ (self, otro):
        a = self.__año + self.__apellido + self.__nombre
        b = otro.__año + otro.__apellido + otro.__nombre
        return a < b 
