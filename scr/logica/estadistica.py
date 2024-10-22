# file: scr/logica/estadistica.py
import math


# Excepción personalizada
class NoSePuedeCalcular(Exception):
    pass


def calcular_media(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía.")

    if not all(isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos de la lista deben ser numéricos.")

    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")

    if len(elementos) == 1:
        return 0.0

    media = calcular_media(elementos)
    suma_diferencias_cuadradas = sum((x - media) ** 2 for x in elementos)
    return math.sqrt(suma_diferencias_cuadradas / len(elementos))
