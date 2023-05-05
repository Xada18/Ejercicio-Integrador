from claseAlumno import Alumno
import numpy as np
import csv

class ManejadorAlumnos:
    __cantidad = 0
    __dimension = 0
    __incremento = 1
    __alumnos = None

    def __init__(self, dimension=0, incremento=1):
        self.__alumnos = np.empty(dimension, dtype= Alumno)
        self.__cantidad = 0
        self.__dimension =  dimension
        self.__incremento = incremento

    def agregarAlumno(self, alumno):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad] = alumno
        self.__cantidad += 1
        

    def carga(self, file):
        archivo = open(file, "r")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for line in reader:
            alumno = Alumno(line[0], line[1], line[2], line[3], line[4])
            self.agregarAlumno(alumno)

        archivo.close()

    def buscarAlumno(self, dni):
        alumno = None
        i = 0
        while alumno == None and i < len(self.__alumnos):
            if self.__alumnos[i].getDNI() == dni:
                alumno = self.__alumnos[i]
            i += 1
                
        return alumno
    
    def ordenar(self):
        
        self.__alumnos.sort()
        
        print("Listado de alumnos:")
        for alumno in self.__alumnos:
            print(alumno)
        print("")


    