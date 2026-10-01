"""
Simulador de Lanzamiento de Dados
=================================

Programa interactivo de consola desarrollado en Python que simula el lanzamiento
de diversos tipos de dados de rol (D4, D6, D8, D10, D12 y D20). 

Permite seleccionar el tipo y la cantidad de dados, mostrando una animación de giro,
los resultados individuales coloreados (críticos, pifias y valores intermedios)
mediante la librería rich, así como el cálculo de la suma acumulada y el promedio.

Autor: Alumno Ruben Barrado Pastor DAM
Módulo: Programación en Python (Optativo) — CFGS Desarrollo de Aplicaciones Multiplataforma (DAM)
"""

import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.live import Live

# Inicialización de consola
consola = Console()

# CONSTANTES: Tipos de dados permitidos (número de caras)
CARAS_D4 = 4
CARAS_D6 = 6
CARAS_D8 = 8
CARAS_D10 = 10
CARAS_D12 = 12
CARAS_D20 = 20


# BUCLE PRINCIPAL DEL PROGRAMA
ejecutando = True

while ejecutando:
    consola.print(Panel.fit("[bold cyan]BIENVENIDO AL SIMULADOR DE DADOS[/bold cyan]", border_style="cyan"))
    print("1. Lanzar dados")
    print("2. Estadísticas ")
    print("3. Salir")

    try:
        opcion = input("Elige una opción: ")
        opcion = int(opcion)
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if opcion == 1:
        print("\n--- TIPOS DE DADOS DISPONIBLES ---")
        print("1. D4  (4 caras)")
        print("2. D6  (6 caras)")
        print("3. D8  (8 caras)")
        print("4. D10 (10 caras)")
        print("5. D12 (12 caras)")
        print("6. D20 (20 caras)")

        caras_input = input("\nIntroduce el número de caras del dado (4, 6, 8, 10, 12, 20): ")

        try:
            caras = int(caras_input)
        except ValueError:
            caras = 0

        if caras == CARAS_D4:
            caras_dado = CARAS_D4
            print(f"Has seleccionado: D4 ({CARAS_D4} caras).")
        elif caras == CARAS_D6:
            caras_dado = CARAS_D6
            print(f"Has seleccionado: D6 ({CARAS_D6} caras).")
        elif caras == CARAS_D8:
            caras_dado = CARAS_D8
            print(f"Has seleccionado: D8 ({CARAS_D8} caras).")
        elif caras == CARAS_D10:
            caras_dado = CARAS_D10
            print(f"Has seleccionado: D10 ({CARAS_D10} caras).")
        elif caras == CARAS_D12:
            caras_dado = CARAS_D12
            print(f"Has seleccionado: D12 ({CARAS_D12} caras).")
        elif caras == CARAS_D20:
            caras_dado = CARAS_D20
            print(f"Has seleccionado: D20 ({CARAS_D20} caras).")
        else:
            print("Tipo de dado no válido.")
            continue

        while True:
            try:
                cantidad_dados = int(input("\n¿Cuántos dados deseas lanzar?: "))
                if cantidad_dados <= 0:
                    print("Advertencia: La cantidad debe ser mayor que 0 (no se admiten números negativos ni cero).")
                else:
                    break
            except ValueError:
                print("Error: Debes introducir un número entero válido.")

        caras_elegidas = caras_dado
        suma_total = 0
        contador_dados = 0
        tiros_realizados = 0

        # Animación de lanzamiento previa al resultado final
        with Live(console=consola, refresh_per_second=10) as live:
            for _ in range(8):
                animacion_texto = "Rodando dados...\n"
                for j in range(cantidad_dados):
                    valor_simulado = random.randint(1, caras_elegidas)
                    animacion_texto += f"Dado {j + 1}: {valor_simulado}\n"
                live.update(Panel.fit(animacion_texto.strip(), border_style="yellow"), refresh=True)
                time.sleep(0.05)

        print("\n--- RESULTADOS DE LA TIRADA ---")
        for i in range(cantidad_dados):
            tirada = random.randint(1, caras_elegidas)
            suma_total += tirada
            contador_dados += 1
            tiros_realizados = tiros_realizados + 1

            if tirada == 1:
                color = "red"
            elif tirada == caras_elegidas:
                color = "green"
            else:
                color = "yellow"

            print(f"Dado {i + 1}: {tirada}")

        # Cálculo del promedio: el operador '/' realiza una división real y produce
        # una conversión implícita de tipo entero (int) a flotante (float).
        promedio = suma_total / cantidad_dados

        print(f"\nTotal acumulado: {suma_total}")
        print(f"Promedio: {promedio:.2f}")
    elif opcion == 2:
        print("\n[!] La opción 'Estadísticas' estará disponible mas tarde.")
        pass
    elif opcion == 3:
        print(" ¡Gracias por usar el Simulador de Dados! ")
        print("          ¡Hasta la próxima!            ")
        ejecutando = False
    else:
        print("Opción incorrecta.")


    


