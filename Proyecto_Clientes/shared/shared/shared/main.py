from views import (
    crear_estudiante,
    listar_estudiantes,
    buscar_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
    agregar_nota,
    materias_ofertadas,
    estudiantes_en_comun
)


while True:

    print()
    print("===== SISTEMA ACADEMICO =====")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Agregar nota")
    print("7. Ver materias ofertadas")
    print("8. Ver materias en comun")
    print("0. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        carnet = input("Carnet: ")

        correcto, mensaje = crear_estudiante(
            nombre,
            apellido,
            email,
            carnet
        )

        print(mensaje)

    elif opcion == "2":

        estudiantes = listar_estudiantes()

        if len(estudiantes) == 0:
            print("No hay estudiantes.")

        else:

            for estudiante in estudiantes:

                print()
                print("ID:", estudiante.id)
                print("Nombre:", estudiante.nombre)
                print("Apellido:", estudiante.apellido)
                print("Email:", estudiante.email)
                print("Carnet:", estudiante.carnet)

    elif opcion == "3":

        texto = input("Ingrese nombre, apellido, email o carnet: ")

        encontrados = buscar_estudiante(texto)

        if len(encontrados) == 0:
            print("No se encontraron estudiantes.")

        else:

            for estudiante in encontrados:

                print()
                print("ID:", estudiante.id)
                print("Nombre:", estudiante.nombre)
                print("Apellido:", estudiante.apellido)
                print("Email:", estudiante.email)
                print("Carnet:", estudiante.carnet)

    elif opcion == "4":

        id = int(input("ID del estudiante: "))

        nombre = input("Nuevo nombre: ")
        apellido = input("Nuevo apellido: ")
        email = input("Nuevo email: ")
        carnet = input("Nuevo carnet: ")

        if actualizar_estudiante(
            id,
            nombre,
            apellido,
            email,
            carnet
        ):
            print("Estudiante actualizado.")

        else:
            print("Estudiante no encontrado.")

    elif opcion == "5":

        id = int(input("ID del estudiante: "))

        if eliminar_estudiante(id):
            print("Estudiante eliminado.")

        else:
            print("Estudiante no encontrado.")

    elif opcion == "6":

        id = int(input("ID del estudiante: "))
        materia = input("Materia: ")
        nota = float(input("Nota: "))

        if nota < 0 or nota > 20:
            print("La nota debe estar entre 0 y 20.")

        else:

            if agregar_nota(id, materia, nota):
                print("Nota agregada.")

            else:
                print("Estudiante no encontrado.")

    elif opcion == "7":

        materias = materias_ofertadas()

        print("Materias:")

        for materia in materias:
            print("-", materia)

    elif opcion == "8":

        id1 = int(input("ID del primer estudiante: "))
        id2 = int(input("ID del segundo estudiante: "))

        comunes = estudiantes_en_comun(id1, id2)

        print("Materias en comun:")

        for materia in comunes:
            print("-", materia)

    elif opcion == "0":

        print("Programa terminado.")
        break

    else:

        print("Opcion incorrecta.")