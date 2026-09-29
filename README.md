# Simulador de Lanzamiento de Dados 🎲

Práctica evaluable para el módulo de Programación (CFGS Desarrollo de Aplicaciones Multiplataforma - DAM).

Esta pequeña aplicación de consola en Python simula tiradas de dados de rol (D4, D6, D8, D10, D12 y D20). El objetivo de la práctica es trabajar con las estructuras de control básicas vistas en clase (bucles, condicionales y control de excepciones con `try/except`), mostrando una interfaz visual y colorida en terminal con la librería `rich`.

## ¿Qué hace el programa?

- Permite elegir el tipo de dado (D4, D6, D8, D10, D12 o D20).
- Pide la cantidad de dados a lanzar, validando que el valor sea un entero positivo (y avisando si metes letras o números inválidos).
- Muestra una breve animación que simula el giro de los dados antes de dar el resultado.
- Muestra el resultado de cada dado con colores:
  - **Verde:** tirada máxima (crítico).
  - **Rojo:** 1 (pifia).
  - **Amarillo:** valores intermedios.
- Calcula y muestra la suma total acumulada y el promedio de la tirada.

> **Nota académica:** El código se ciñe a los contenidos de las unidades UT1 y UT2, por lo que no utiliza funciones personalizadas (`def`), listas, diccionarios ni objetos.

---

## Inicialización del repositorio

Para inicializar el repositorio Git en la carpeta del proyecto desde la terminal:

```bash
git init
```

*(Opcional: para enlazarlo con tu repositorio remoto de GitHub y hacer el primer commit)*:
```bash
git add README.md
git commit -m "Commit inicial: añadido README del proyecto"
git branch -M main
git remote add origin <URL_DE_TU_REPOSITORIO>
git push -u origin main
```

---

## Instalación y ejecución

1. **Crear y activar el entorno virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # En Linux / macOS
   # .venv\Scripts\activate     # En Windows
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el simulador:**
   ```bash
   python3 simulador_dados.py
   ```