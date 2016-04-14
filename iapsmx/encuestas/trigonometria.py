# -*- coding: utf-8 -*-

from math import *
# donde adyacente es la valencia y el opuesto es arousal
def calculaAngulo(adyacente, opuesto):
    # angulo = degrees(atan(opuesto/adyacente))

    if opuesto == 0 and adyacente == 0:
        return 0.0
    # si no hay cateto opuesto y el adyacente es -
    elif opuesto == 0 and adyacente < 0:
        return 180.0
    # si no hay adyacente y el opuesto es -
    elif adyacente == 0 and opuesto < 0:
        return 270.0
    # los 90 y 0 grados si los calcula automaticamente

    # calculando hipotenusa.
    # se utiliza el seno porque tan en 90 grados es infinito
    h = hypot(abs(opuesto), abs(adyacente))
    angulo = degrees(asin(opuesto / h))

    # si esta en el segundo cuadrante
    if adyacente < 0 and opuesto > 0:
        angulo = 180 - angulo

    # si esta en el 3 cuadrante
    elif opuesto < 0 and adyacente < 0:
        angulo = abs(angulo) + 180.0

    # si esta en el cuarto cuadrante
    elif adyacente > 0 and opuesto < 0:
        angulo += 360.0

    return angulo
