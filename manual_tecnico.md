# 1. Portada
Pendiente para entrega final en pdf.

# 2. Requerimientos Tecnicos
Lenguaje: Python 3.13
Sistemas operativos: Windows, macOS
Editor utilizado: VS Code

# 3. Descripción Técnica General
El Gestor de Notas Académicas es una aplicación de interfaz en línea de comandos desarrollada íntegramente en Python 3. Esta diseñado para ser autocontenido y así no depender de librerías externas.
La arquiteactura del programa es de sesión única por lo que es únicamente para pruebas ya que se mantiene en la memoria RAM durante su ejecución. El flujo principal está controlado por un bucle While que presenta el menú interactivo al usuario infinitamente para gestionar las llamadas a las funciones correspondientes o hasta que se desee cerrar el programa.

# 4. Estructura General del Código
El codigo fuente está contenido en el archivo main.py, sigue un paradigma de programación modular para promover la legibilidad y el mantenimiento o también mejoras del mismo.

La estructura de datos principal está definido en una lista global 'cursos = []' al inicio del programa. Esta lista funciona como la base de datos en memoria para todo el programa, almacenado en ella los registros de los cursos agregados, editados, eliminados y todas las funciones incluídas.

Un bucle While True al final de archivo actúa como motor de la aplicación, ya que es el encargado de mostrar el menú, leer la opción ingresada por el usuario y así llamar a cada función. Se utiliza una estructura condicional if/elif/else para la invoación de cada una de las funciones.


# 5. Descripcion de Funciones


# 6. Estructura de Datos
La estructura de datos utilizada es una Lista de Diccionarios, así:
cursos = [
    {'nombre': 'Precalculo', 'nota': 80.00},
    {'nombre': 'Algoritmos', 'nota': 75.00},
]

La lista se utiliza como contenedor principal, ya que al ser dinámica nos permite agregar (.append()), eliminar (.pop()) elementos fácilmente.

Se utilizan diccionarios en cada elemento de la lista para así ser fácilmente accesible a cada clave (nombre, nota) y también tiene la ventaja de ser auto descriptivo y fácilmente también se pueden añadir campos nuevos con solo agregar una nueva clave al diccionario.

# 7. Algoritmos Implementados
Busqueda lineal: Se utiliza en las funciones de búsqueda por nombre exacto (opción 7), actualización (opción 3) y eliminación (opción 4). Este algoritmo itera secuencialmente sobre el diccionario de {cursos} desde el indice 0 hasta el último, también utilizando (.lower()) para que sea insensible a mayúsculas y minúsculas.

Busqueda binaria: Utilizada en la opción 10, busca cursos por nombre, requiere que la lista este ordenada, utilizando la función (sorted()). Su eficiencia radica en que va dividiendo el espacio de búsqueda a la mitad en cada iteración, esto resulta en una complejidad de O(log n), siendo significativamente más rápida que la búsqueda lineal.

Ordenamiento Burbuja: Implementado en la función 9, ordena los cursos según su nota en orden descendente. Utiliza una copia del diccionario principal para no alterar su registro original.

Ordenamiento por Inserción: Utilizada en la función 8, ordena los cursos alfabéticamente y también opera sobre una copia del diccionario original. Su lógica se basa en construir una sublista ordenada e inserta secuencialmente los elementos restantes en su posición correcta.