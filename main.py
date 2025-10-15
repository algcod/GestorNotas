#Lista principal para almacenar los cursos
cursos = []

#Copia de lista principal utilizada para las soicitudes de revision
cola_revision = []

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

def mostrar_cursos(lista_a_mostrar):
    #funcion para mostrar todos los cursos registrados
    print("\n--- LISTA DE CURSOS ---")
    if not lista_a_mostrar:
        print("Aun no hay cursos para mostrar.")
        return
    print(f"{'Curso':<25} | {'Nota'}")
    print("-" * 35)
    for curso in lista_a_mostrar:
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
        if curso['nota'] >= 60:
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"Total de cursos: {len(cursos)}")
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_curso_lineal():
    #funcion para buscar cursos usando busquda lineal

    print("\n7. BUSCAR CURSO POR NOMBRE (BUSQUEDA LINEAL)")
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
        mostrar_cursos([curso_encontrado])

def ordenar_por_nombre():
    #funcion para ordenar los cursos por nombre utilizando el metodo de insercion
    print("\n8. ORDENAR CURSOS POR NOMBRE (A-Z)")
    if not cursos:
        print("No hay cursos para ordenar")
        return
    copia_cursos = cursos.copy()
    n = len(copia_cursos)
    for i in range(1, n):
        clave = copia_cursos[i]
        j = i - 1
        while j >= 0 and clave['nombre'].lower() < copia_cursos[j]['nombre'].lower():
            copia_cursos[j + 1] = copia_cursos[j]
            j -= 1
        copia_cursos[j + 1] = clave
    mostrar_cursos(copia_cursos)

def ordenar_por_nota():
    #funcion para ordenar los cursos por notas utilizando el metodo burbuja

    print("\n9. ORDENAR CURSOS POR NOTA (Mayor a Menor)")
    if not cursos:
        print("No hay cursos para ordenar")
        return
    
    copia_cursos = cursos.copy()
    n = len(copia_cursos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if copia_cursos[j]['nota'] < copia_cursos[j + 1]['nota']:
                copia_cursos[j], copia_cursos[j + 1] = copia_cursos[j + 1], copia_cursos[j]
    
    mostrar_cursos(copia_cursos)

def buscar_curso_binaria():
    #Funcion para buscar curos utilizando la busqueda binaria

    print("\n10. BUSCAR CURSO POR NOMBRE")
    if not cursos:
        print("No hay cursos en los cuales buscar")
        return
    
    #Crear y ordenar por nombre una copia de la lista
    lista_ordenada = sorted(cursos, key=lambda curso: curso['nombre'].lower())

    nombre_buscar = input("Ingrese el nombre completo del curso que necesita buscar: ")

    curso_encontrado = None
    bajo = 0
    alto = len(lista_ordenada) - 1

    while bajo <= alto:
        medio = (alto + bajo) // 2
        nombre_medio = lista_ordenada[medio]['nombre'].lower()
        
        if nombre_medio < nombre_buscar.lower():
            bajo = medio + 1
        elif nombre_medio > nombre_buscar.lower():
            alto = medio - 1
        else:
            curso_encontrado = lista_ordenada[medio]
            break
    if not curso_encontrado:
        print(f"No se encontro un curso con el nombre '{nombre_buscar}'")
    else:
        print("\nCurso encontrado!")
        mostrar_cursos([curso_encontrado])

def solicitudes_revision():
    #funcion para crear solicitudes para revision de cursos

    while True:
        print("\n11. SOLICITUDES DE REVISION")
        print("1. Agregar solicitud para revision")
        print("2. Procesar siguientes solicitud")
        print("3. Ver solicitudes pendientes")
        print("4. Volver al menu principal")

        opcion_cola = input("Seleccione luna opcion de la cola: ")

        if opcion_cola == '1':
            nombre_curso = input("Ingrese el nombre del curso para revision: ")
            if nombre_curso.strip():
                cola_revision.append(nombre_curso)
                print(f"Solicitud para '{nombre_curso}' agregada a la cola")
            else:
                print("El nombre del curso no puede estar vacio")
        
        elif opcion_cola == '2':
            if not cola_revision:
                print("NO hay solicitudes de revision pendientes")
            else:
                curso_procesado = cola_revision.pop(0)
                print(f"Procesando solicitud de revision par: '{curso_procesado}'")
                print("Solicitud procesada y eliminada de la cola")
    


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
        mostrar_cursos(cursos) #Llamamos funcion para mostrar los cursos

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
        ordenar_por_nombre() #Llamamos funcion para ordenar los cursos por nombre utilizando el metodo de insercion

    elif opcion == '9':
        ordenar_por_nota() #Llamamos funcion para ordenar los cursos por nota por el metodo de burbuja

    elif opcion == '10':
        buscar_curso_binaria() #Llamamos funcion para buscar cursos por su nombre mediante la busqueda binaria
    
    elif opcion == '11':
        solicitudes_revision() #Llamamos funcion para hacer las solicitudes de revision de cursos

    elif opcion == '12':
        print("Trabajando...")
        
    elif opcion == '13':
        print("\nGracias por usar el Gestor de Notas Academicas")
        break
    else:
        print("\nOpcion invalida, intente de nuevo.")
