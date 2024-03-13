
# autor: michel
# data 13/03/2024

import math

# area_circulo = lambda raio: 3.1415 * raio**2
area_circulo = lambda raio: math.pi * math.pow(raio, 2)

raio = 5
area = area_circulo(raio)
print(f"Área do círculo: {area}") # Área do círculo: 78.53981633974483
