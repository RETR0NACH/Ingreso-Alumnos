
curso = []
alumnos = []
def agregarAlumnos(coleccion):

    nombre = input("Ingrese el nómbre del alumno--->")
    apellido = input("Ingrese el apellido del alumno--->")
    nivel  = input("Ingrese el curso del alumno--->")
    promedio = input("Ingrese el promedio del alumno--->")

    coleccion.append([nombre, apellido, nivel, promedio])

    print("Se ha ingresado correctamente el alumno :)")
    for estudiante in coleccion:
        print(estudiante)

def mostrarCurso(curso):
    contador = 1
    print(" NOMBRE | APELLIDO |  CURSO | PROMEDIO ")
    for alumnos in curso:
        print(f"{contador}.-{alumnos[0]} | {alumnos[1]} | {alumnos[2]} | {alumnos[3]}")
        contador = contador + 1

def eliminarAlumno(coleccion):
    try:
        alumnoEliminar = input("Ingrese el nombre del alumno que desea eliminar: ")
    except ValueError:
        print("ERR0r.. vuelva a intenar")

    for estudiante in coleccion:
        if estudiante[0] == alumnoEliminar:
            coleccion.remove(estudiante)
            print(f"El alumno {alumnoEliminar} ha sido eliminado correctamente.")
            break
    else:
        print(f"No se encontró al alumno {alumnoEliminar}.")

def guardarAlumno(curso):
    # Creación de archivo TXT
    with open('AlumnosIngresados.txt', 'w', encoding='utf-8', newline='') as archivo:
        archivo.write(f"{'| NOMBRE |': <20}{'| APELLIDO |':<20}{'| CURSO |': <20}{'| PROMEDIO |':<20}\n")  # Agregamos \n al final
        archivo.write("-" * 100 + "\n")  # Línea de separación 
        for alumnos in curso:
            archivo.write(f"{alumnos[0]: <20}{alumnos[1]: <20}{alumnos[2]: <20}{alumnos[3]: <20}\n")  # Agregamos \n al final

def modificarEstudiante():
    mostrarCurso()
    posicion = int(input("Ingresa el número que quieras modificar--->"))
    print(f"El curso para modificar un estudiante es {curso[posicion-1]}")
    try:
        nombreNuevo = input("Ingresa el nómbre del estudiante--->")
        apellidoNuevo = input("Ingresa el apellido del estudiante--->")
        cursoNuevo = input("Ingresa el curso del estudiante--->")
        promedioNuevo = input("Ingresa el promedio del estudiante--->")
    except ValueError:
        print("ERR0R=!#... Intentelo de nuevo.")

    curso[posicion-1] = [nombreNuevo, apellidoNuevo, cursoNuevo, promedioNuevo]
    print("Se modificó el estudiante correctamente.")
