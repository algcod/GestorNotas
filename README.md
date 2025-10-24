# GestorNotas
Proyecto algoritmos para gestionar notas académicas

# Redacción del problema
El Gestor de Notas académicas es un programa diseñado para que un estudiante administre sus calificaciones de forma eficiente desde la consola. Este programa permite registrar, visualizar, modificar, eliminar y analizar las notas de los cursos, esto facilita el seguimiento académico. El programa aborda la necesidad de organizar información académica de manera clara, promoviendo la usabilidad y la simplicidad, utilizando un menú interactivo pero sencillo de entender.

# Requisitos del sistema
- Registro de cursos: Ingresar nombre del curso y nota.
- Visualización: Mostrar todos los cursos con sus notras.
- Análisis: Permite calcular el promedio general, así como mostrar los cursos aprobados y reprobados.
- Búsquda: Permite buscar los cursos.
- Ordenamiento: Ordenar los cursos por nota y por nombre.
- Estructuras: Utiliza pilas para historiales.
- Modificación y eliminación: Actualización de notas y eliminación de cursos.
- Salida: Finaliza la sesión.

# Requisitos no funcionales
- Debe ejecutarse únicamente en Python.
- Código modulado con funcionaes claras y comentadas.
- Validación para las entradas de las notas.
- Mensajes claros y manejo de errores.

# Diseño del menú
```text
---------------------------------------------------------
              Sistema de Gestión Académica 
---------------------------------------------------------
Gestión de Cursos
  1. Agregar nuevo curso
  2. Ver todos los cursos
  3. Actualizar nota
  4. Eliminar curso
     
Análisis Académico
  5. Calcular promedio general
  6. Cursos aprobados y reprobados
  
Búsqueda y Ordenamiento
  7. Buscar curso (por coincidencia)
  8. Ordenar por nombre
  9. Ordenar por nota
  10. Buscar curso
  
Estructuras de Datos
  11. Cola de solicitudes de revisión
  12. Historial de cambios
  
Salida
  13. Salir del sistema
-------------------------------------------------------
Ingrese una opción (1 - 13):
```
# Detalles de las funciones agregadas
El programa usa un diseño modular simple.
- Se utiliza una única lista global "cursos".
- Cada funcionalidad del menú está en su propia función y llamada desde el menú principal utilizando un bucle que repite hasta que seleccionemos salir del programa.
- Se utilizan diccionarios para almacenar en "cursos" cada uno junto a su nota, así al buscar uno por nombre como se solicita en unos puntos del menú se ubiquen y junto al nombre del curso, la nota correspondiente.
- Se utiliza .lower() en ciertas funciones para no importando la introducción de texto de parte del usuario siga leyendo los datos solicitados.
- Se utiliza try-except, ValueError para evitar errores al no ingresar una entrada no válida.

# Reflexión Personal
A. ¿Qué aprendí con este proyecto?
  Con este proyecto aprendí a estructurar una aplicación con Python desde cero, implementando lo aprendido en clases, complementando con información buscada personalmente, y así como fuimos viendo como implementar practicas de algoritmos, métodos de ordenamiento, búsquedas, aplicar las estructuras de datos como pilas, colas, también en el manejo de errores, ya que a la prueba y error poco a poco se iba mejorarndo el proyecto.

B. ¿Qué fue lo más desafiante de resolver?
  En general todo el proyecto, sí vimos en clase todo lo incluído en el proyecto, pero claramente es muy diferente el practicar ejercicios cortos ha ya ir creando muchas funciones y complementarlas o usarlas en cada función del menú prinpal,y aunque no interfieran como tal entre funciones, si utilizamos las mismas listas y juntas todas las funciones se van complementando para ir funcionando en cada función de todo el menú. 
  Lo más complicado del proyecto fue ir uniendo cada parte de las distintas funciones, como a la hora de integrar la función del historial de cambios, se complica al necesitar modificar otras funiones para que se complementen, también con la búsqueda binaria que al no necesitar modificar la lista original.

C. ¿Qué mejoraría si tuviera más tiempo?
  La mejora que veo necesaria sería guardar los datos ingresados, para que al abrir el programa de nuevo pueda ver mis datos ingresados en la sesión anterior, ahora no se pedía pero creo que es una función que me gustaría tener.
  Y me gustaría hacerlo más gráfico también, quizá no con dibujos pero no dejarlo únicmente así como en forma de lista todo como lo vemos cuando lo ejecutamos.