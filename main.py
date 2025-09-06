#Lista principal para almacenar los cursos
cursos = []

def registrar_curso():
    #funcion para agregar un curso nuevo, pide nombre, no y lo valida

    print("\n--- 1. Agregar Nuevo Curso ---")

    #Validacion del nombre del curso
    while True:
        nombre = input("Ingrese el nombre del curso: ")
        if nombre.strip():
            break
        else:
            print("Error: El nombre del curso no puede estar vacio.")

    #Validacion de la nota del curso a ingresar
    while True:
        try:
            nota_str = input(f"Ingrese la nota para '{nombre}' (0-100): ")
            nota = float(nota_str)
            if 0 <= nota <= 100:
                break
            else:
                print("Error: La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Ingrese un valor numerico.")

    #Guardar el curso en nuestra lista
    nuevo_curso = {'nombre': nombre, 'nota': nota}
    cursos.append(nuevo_curso)

    print(f"\nCurso '{nombre}' agreagado con exito!")
    
#Menu
while True:
    print("\nSISTEMA DE GESTION ACADEMICA")
    print("1. Agregar nuevo curso")
    print("2. Ver todos los cursos")
    print("3. Actualizar nota")
    print("4. Eliminar curso")
    print("5. Calcular promedio general")
    print("6. Cursos aprobados y reprobados")
    print("7. Buscar curso (por coincidencia)")
    print("8. Ordenar por nombre")
    print("9. Ordenar por nota")
    print("10. Buscar curso")
    print("11. Cola de solicitudes de revision")
    print("12. Historial de cambios")
    print("13. Salir del sistema")

    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        registrar_curso() #Llamamos funcion para agregar cursos nuevos

    elif opcion == '2':
        print("Trabajando...")

    elif opcion == '13':
        print("\nGracias por usar el Gestor de Notas Academicas")
        break
    else:
        print("\nOpcion invalida, intente de nuevo.")
