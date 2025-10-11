# 1. Portada
Pendiente para entrega final en pdf.

# 2. Descripción Técnica General
El Gestor de Notas Académicas es una aplicación de interfaz en línea de comandos desarrollada íntegramente en Python 3. Esta diseñado para ser autocontenido y así no depender de librerías externas.
La arquiteactura del programa es de sesión única por lo que es únicamente para pruebas ya que se mantiene en la memoria RAM durante su ejecución. El flujo principal está controlado por un bucle While que presenta el menú interactivo al usuario infinitamente para gestionar las llamadas a las funciones correspondientes o hasta que se desee cerrar el programa.

# 3. Estructura General del Código
El codigo fuente está contenido en el archivo main.py, sigue un paradigma de programación modular para promover la legibilidad y el mantenimiento o también mejoras del mismo.

La estructura de datos principal está definido en una lista global 'cursos = []' al inicio del programa. Esta lista funciona como la base de datos en memoria para todo el programa, almacenado en ella los registros de los cursos agregados, editados, eliminados y todas las funciones incluídas.

Cada funcionalidad del sistema está encapsulada en una función dedicada. Como registrar_curso() que es utilizado para agregar cursos a la lista anteriormente mostrada.
Este enfoque asegura que cada función tenga una única y clara responsabilidad.

Un bucle While True al final de archivo actúa como motor de la aplicación, ya que es el encargado de mostrar el menú, leer la opción ingresada por el usuario y así llamar a cada función. Se utiliza una estructura condicional if/elif/else para la invoación de cada una de las funciones.

# 4. Estructura de Datos
La estructura de datos utilizada es una Lista de Diccionarios, así:
cursos = [
    {'nombre': 'Precalculo', 'nota': 80.00},
    {'nombre': 'Algoritmos', 'nota': 75.00},
]

La lista se utiliza como contenedor principal, ya que al ser dinámica nos permite agregar (.append()), eliminar (.pop()) elementos fácilmente.

Se utilizan diccionarios en cada elemento de la lista para así ser fácilmente accesible a cada clave (nombre, nota) y también tiene la ventaja de ser auto descriptivo y fácilmente también se pueden añadir campos nuevos con solo agregar una nueva clave al diccionario.

# 5. Algoritmos Implementados
Busqueda lineal