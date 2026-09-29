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

# CONSTANTES: Tipos de dados permitidos (número de caras)
D4 = 4
D6 = 6
D8 = 8
D10 = 10
D12 = 12
D20 = 20

# BUCLE PRINCIPAL DEL PROGRAMA
ejecutando = True

while ejecutando:
    print("    BIENVENIDO AL SIMULADOR DE DADOS    ")
    


