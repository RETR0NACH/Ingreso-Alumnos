import funciones as fun
curso = []
alumnos = []
while True:
    print(" ______________________")
    print("| REGISTRO ESTUDIANTES |")
    print("|1.-Agregar un alumno  |")
    print("|2.-Mostrar un alumno  |")
    print("|3.-Eliminar alumno    |")
    print("|4.-Guardar datos      |")
    print("|5.-Modificar Alumono  |")
    print("|6.-Salir del programa |")
    print("|______________________|")
    try:
        opc = int(input("Ingrese una opción--->"))
    except:
        print("ERR0r... vuelva a intentarlo.")

    if (opc ==1):
        fun.agregarAlumnos(curso)
    elif (opc ==2):
        fun.mostrarCurso(curso)
    elif (opc == 3):
        fun.eliminarAlumno(curso)
    elif (opc == 4):
        fun.guardarAlumno(curso)
    elif (opc == 5):
        fun.modificarEstudiante()
    elif (opc == 6):
        print("Muchas gracias por utilizar nuestro programa, Suerte :)")
        break
    else:
        break