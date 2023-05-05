from claseManejadorAlumnos import ManejadorAlumnos
from claseManejadorMaterias import ManejadorMaterias
from claseMenu import Menu


if __name__ == '__main__':

    archivo1 = "alumnos.csv"
    archivo2 = "materiasAprobadas.csv"

    Alumnos = ManejadorAlumnos()
    Alumnos.carga(archivo1)
    Materias = ManejadorMaterias()
    Materias.carga(archivo2)
    MenuSIU = Menu()
    ban = True
    while ban:
        op = MenuSIU.select(Alumnos, Materias)
        if op == "0":
            ban = False
        elif op != "1" and op != "2" and op != "3":
            print("Opcion no valida")
        


