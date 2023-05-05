
class Menu:
    __opcion = ""

    def select (self, alumnos, materias):

        print("Menu:")
        print("1 - Promedio con y sin aplazos")
        print("2 - Listado alumnos promocionales")
        print("3 - Listado de alumnos")
        print("0 - Salir")
        self.__opcion = input("Elija una opcion: ")

        if self.__opcion == "1":
            dni = input("Ingrese DNI: ") 
            alumno = alumnos.buscarAlumno(dni)
            if alumno == None:
                print("No se encontro el alumno")
            else:
                promCon = materias.promedioConAplazos(dni)
                if promCon == 0:
                    print("No se encontro ninguna materia del alumno con ese DNI")
                else:
                    print(f"Promedio con aplazos:{promCon: .2f}")
                    promSin = materias.promedioSinAplazos(dni)
                    if promSin == 0:
                        print("El alumno no tiene promedio sin aplazos")
                    else:
                        print(f"Promedio sin aplazos:{promSin: .2f}")
            print("")

        elif self.__opcion == "2":
            materia = input("Ingrese el nombre de la materia: ")
            print(f"Listado de alumnos promocionales de la materia {materia}")
            materias.promocionales(alumnos, materia)
            print("")
            
        elif self.__opcion == "3":
            alumnos.ordenar()

        return self.__opcion