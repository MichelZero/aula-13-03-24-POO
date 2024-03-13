
# autor: michel
# data 13/03/2024
# 

# 4. Filtrar uma lista de números pares.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))

print(numeros_pares) # [2, 4, 6, 8, 10]
