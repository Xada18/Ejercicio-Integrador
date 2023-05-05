from claseMateria import Materia
import csv

class ManejadorMaterias:
    __materias = []

    def __init__(self):
        self.__materias = []

    def carga(self, file):
        archivo = open(file, "r")
        lector = csv.reader(archivo, delimiter=";")

        next(lector)

        for linea in lector:
            materia = Materia(linea[0], linea[1], linea[2], int(linea[3]), linea[4])
            self.__materias.append(materia)
        
        archivo.close()


    def promedioConAplazos(self, dni):
        suma = 0
        cont = 0

        for materia in self.__materias:
            if dni == materia.getDNI():               
                suma += materia.getNota()
                cont += 1
                
        if suma == 0:
            promedio = 0
        else:
            promedio = suma/cont
            
        return promedio


    def promedioSinAplazos(self, dni):
        suma = 0
        cont = 0

        for materia in self.__materias:
            if dni == materia.getDNI() and materia.getNota() >= 4:               
                suma += materia.getNota()
                cont += 1
                
        if suma == 0:
            promedio = 0
        else:
            promedio = suma/cont
            
        return promedio


    def promocionales(self, alumnos, materia):
        ban = 0
        for m in self.__materias:
            if m.getNombre() == materia:
                if m.getAprobacion() == "P":
                    dni = m.getDNI()
                    alumno = alumnos.buscarAlumno(dni)
                    ban = 1
                    print(f"{dni}, {alumno.getApellido()} {alumno.getNombre()}, {m.getFecha()}, {m.getNota()}, {alumno.getAño()}")
        
        if ban == 0:
            print("No hubo alumnos promocionales en esta materia")

            