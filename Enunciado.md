# Práctica Evaluable: Simulador de Lanzamiento de Dados
**Módulo:** Programación en Python (Optativo) — CFGS Desarrollo de Aplicaciones Multiplataforma (DAM)  
**Resultados de Aprendizaje Evaluados:**
* **RA1:** Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje.
* **RA2:** Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

---

## 1. Enunciado

Crea una aplicación interactiva de consola en Python que simule el lanzamiento de dados de distintos tipos (**D4, D6, D8, D10, D12 y D20**).

El programa debe permitir al usuario:
1. Elegir el tipo de dado que quiere lanzar.
2. Indicar cuántos dados quiere lanzar.
3. Ver los resultados de forma visual y colorida, usando la librería `rich`.
4. Ver una breve animación que simule el proceso de rodar los dados antes de mostrar el resultado final.

---

## 2. Requisitos Funcionales y Técnicos

El programa debe cumplir rigurosamente los siguientes requisitos:

1. **Menú principal:**
   * Un bucle que muestre un menú con al menos las opciones *"Lanzar dados"* y *"Salir"*.
   * Debe repetirse de forma continua hasta que el usuario decida salir expresamente.

2. **Selección del tipo de dado:**
   * Mediante una estructura condicional (`if` / `elif` / `else`), a partir del número de caras de cada tipo de dado (D4, D6, D8, D10, D12, D20).
   * Los valores de las caras deben estar definidos mediante **constantes**.

3. **Validación de la cantidad de dados:**
   * Se debe solicitar por teclado cuántos dados se desean lanzar.
   * Se debe controlar el caso de que el usuario introduzca un texto no numérico o valores no válidos.
   * Se debe insistir y repetir la petición hasta obtener un número entero positivo válido ($> 0$).

4. **Animación del lanzamiento:**
   * Antes de mostrar el resultado definitivo, el programa debe mostrar varias veces valores aleatorios cambiando rápidamente para simular el giro de los dados.
   * Debe implementarse mediante los componentes de animación de `rich` (por ejemplo, `Live` y `Panel`) combinados con pausas breves de tiempo.

5. **Resultado coloreado:**
   * Cada valor obtenido individualmente debe mostrarse con un color representativo:
     * **Verde:** si es el valor máximo posible del dado (éxito crítico).
     * **Rojo:** si es un 1 (pifia / valor mínimo).
     * **Amarillo:** cualquier otro caso intermedio.
   * Debe presentarse junto con el total acumulado de la tirada dentro de un `Panel` de `rich`.

6. **Cálculo del promedio:**
   * Además del total acumulado, debe calcularse y mostrarse el promedio de los valores obtenidos (total dividido entre la cantidad de dados lanzados).

7. **Uso de `pass`:**
   * En algún punto del programa debe usarse la sentencia `pass` como marcador de una futura ampliación pendiente de desarrollo (por ejemplo, una opción reservada para *"Ver estadísticas"*).

8. **Control de excepciones adicional:**
   * Cualquier entrada del usuario susceptible de provocar un error en tiempo de ejecución (como introducir texto en el menú principal) debe controlarse mediante bloques `try` / `except`, evitando en todo momento que el programa aborte de forma inesperada.

9. **Documentación del código:**
   * El script debe incluir un docstring de módulo al inicio que describa su propósito.
   * Los bloques principales deben contar con comentarios claros y explicativos.

---

## 3. Restricciones Académicas Importantes

* **Materias permitidas:** Exclusivamente las estructuras y elementos del lenguaje tratados en la **UT1** y **UT2** (variables, tipos básicos `int`, `float`, `str`, `bool`, operadores aritméticos/lógicos/relacionales, `if`/`elif`/`else`, bucles `for`/`while`, sentencias `break`, `continue`, `pass` y control de excepciones `try`/`except`).
* **Herramientas NO permitidas:** Queda terminantemente prohibido utilizar herramientas del lenguaje aún no tratadas en clase, tales como:
  * Funciones definidas por el propio alumno (`def`).
  * Listas (`[]`), tuplas (`()`), diccionarios (`{}`) o conjuntos.
  * Clases y Programación Orientada a Objetos.
* **Librería externa autorizada:** Se permite y exige el uso normal de la librería externa `rich`, ya que su utilización no computa como estructura interna avanzada evaluada.

---

## 4. Requisitos de Entrega

1. **Estructura del Proyecto:**
   * Desarrollado en un entorno de desarrollo integrado (como Visual Studio Code).
   * Proyecto configurado con su propio entorno virtual (`venv`).
   * Instalación de dependencias reflejada en un archivo `requirements.txt`.
   * Código fuente centralizado en un único archivo ejecutable (`simulador_dados.py`).

2. **Control de Versiones (GitHub):**
   * El desarrollo debe realizarse utilizando un repositorio propio en GitHub.
   * El historial de commits debe reflejar un desarrollo incremental paso a paso desde el inicio del proyecto hasta su conclusión.

3. **Material a Entregar en Aula Virtual:**
   * URL al repositorio público de GitHub con el historial de commits.
   * Archivo comprimido (`.zip` o `.tar`) con la carpeta del proyecto local: código `.py`, archivo `requirements.txt` y carpeta del entorno virtual.
   * Vídeo demostrativo con un mínimo de tres ejecuciones de prueba distintas, cubriendo al menos un caso límite (entradas no numéricas, cantidades inválidas o valores mínimos).