#Lista principal para almacenar los cursos
cursos = []

def registrar_curso():
    #funcion para agregar un curso nuevo, pide nombre, nota y lo valida

    print("\n1. AGREGAR NUEVO CURSO")

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

def mostrar_curso():
    #funcion para mostrar todos los cursos registrados

    print("\n2. VER TODOS LOS CURSOS")

    if not cursos:
        print("Aun no hay cursos registrados")
        return
    print(f"{'Curso':<25} | {'Nota'}")
    print("-" * 35)

    for curso in cursos:
        nombre = curso['nombre']
        nota = curso['nota']
        print(f"{nombre:<25} | {nota}")

def actualizar_nota():
    #funcion para buscar un curso y editar la nota

    print("\n3. ACTUALIZAR NOTA")

    if not cursos:
        print("Aún no hay cursos para actualizar")
        return

    nombre_buscar = input("Ingrese el nombre del curso que desea actualizar: ")
    
    curso_encontrado = None
    for curso in cursos:
        if curso['nombre'].lower() == nombre_buscar.lower():
            curso_encontrado = curso
            break
    
    if curso_encontrado:
        print(f"Nota actual de '{curso_encontrado['nombre']}': {curso_encontrado['nota']}")
        while True:
            try:
                nueva_nota_str = input("Ingrese la nueva nota (0-100): ")
                nueva_nota = float(nueva_nota_str)
                if 0 <= nueva_nota <= 100:
                    # Actualizamos la nota del curso que buscamos
                    curso_encontrado['nota'] = nueva_nota
                    print("\n¡Nota actualizada correctamente!")
                    break
                else:
                    print("Error: La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico")
    else:
        print(f"Error: No se encontró un curso con el nombre '{nombre_buscar}'")

def eliminar_curso():
    #funcion para buscar un curso y eliminarlo de nuestro gestor
 
    print("\n4. ELIMINAR CURSO")
    if not cursos:
        print("No hay cursos para eliminar")
        return

    nombre_buscar = input("Ingrese el nombre del curso que desea eliminar: ")
    
    indice_encontrado = -1
    for i, curso in enumerate(cursos):
        if curso['nombre'].lower() == nombre_buscar.lower():
            indice_encontrado = i
            break
            
    if indice_encontrado != -1:
        curso_eliminar = cursos[indice_encontrado]
        print(f"Curso encontrado: {curso_eliminar['nombre']} - Nota: {curso_eliminar['nota']}")
        
        confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ")
        
        if confirmacion.lower() == 's':
            # Eliminamos el curso de la lista usando su índice
            cursos.pop(indice_encontrado)
            print("Curso eliminado correctamente")
        else:
            print("Operación cancelada")
    else:
        print(f"Error: No se encontró un curso con el nombre '{nombre_buscar}'")

def calcular_promedio():
    #funcion para calcular el promedio de las notas de los cursos ingresados

    print("\n5. CALCULAR PROMEDIO GENERAL")
    if not cursos:
        print("No hay notas para calcular un promedio")
        return
    
    suma_notas = 0
    for curso in cursos:
        suma_notas += curso['nota']

    total_cursos = len(cursos)

    promedio = suma_notas / total_cursos

    print(f"El promedio general de los {total_cursos} cursos es: {promedio:.2f}")

def contar_cursos():
    #funcion para contar cursos aprobados y reprobados

    print("\n6. CUROS APROBADOS Y REPROBADOS")
    if not cursos:
        print("No hay cursos registrados")
        return
    aprobados = 0
    reprobados = 0

    for curso in cursos:
        if curso['nota'] > 60:
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"Total de cursos: {len(cursos)}")
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_curso_lineal():
    #funcion para buscar cursos usando busquda lineal

    print("\n7. BUSCAR CURSO POR NOMBRE (BUSQUEA LINEAL)")
    if not cursos:
        print("No hay cursos registados")
        return
    
    nombre_buscar = input("Ingrese el nombre completo del curso que desea buscar: ")

    curso_encontrado = None
    for curso in cursos:
        if nombre_buscar.lower() == curso['nombre'].lower():
            curso_encontrado = curso
            break
    
    if not curso_encontrado:
        print(f"No se encontro un curso con el nombre '{nombre_buscar}'")
    else:
        print("\nCurso Encontrado")
        print(f"{'Curso':<25} | {'Nota'}")
        print("-" * 35)
        nombre = curso_encontrado['nombre']
        nota = curso_encontrado['nota']
        print(f"{nombre:<25} | {nota}")

#Menu
while True:
    print("\nSISTEMA DE GESTION ACADEMICA")
    print("1. Agregar nuevo curso")
    print("2. Ver todos los cursos")
    print("3. Actualizar nota")
    print("4. Eliminar curso")
    print("5. Calcular promedio general")
    print("6. Cursos aprobados y reprobados")
    print("7. Buscar curso por nombre (Busqueda Lineal)")
    print("8. Ordenar por nombre")
    print("9. Ordenar por nota")
    print("10. Buscar curso por nombre (Busqueda Binaria)")
    print("11. Cola de solicitudes de revision")
    print("12. Historial de cambios")
    print("13. Salir del sistema")

    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        registrar_curso() #Llamamos funcion para agregar cursos nuevos

    elif opcion == '2':
        mostrar_curso() #Llamamos funcion para mostrar los cursos

    elif opcion == '3':
        actualizar_nota() #Llamamos funcion para edicion de nota

    elif opcion == '4':
        eliminar_curso() #Llamamos funcion para eliminar cursos

    elif opcion == '5':
        calcular_promedio() #Llamamos funcion para calcular promedio de los cursos

    elif opcion == '6':
        contar_cursos() #Llamamos funcion para contar cursos aprobados y reprobados  

    elif opcion == '7':
        buscar_curso_lineal() #Llamamos funcion para buscar cursos usando la busqueda lineal

    elif opcion == '8':
        print("Trabajando...")

    elif opcion == '13':
        print("\nGracias por usar el Gestor de Notas Academicas")
        break
    else:
        print("\nOpcion invalida, intente de nuevo.")
