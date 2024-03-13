
# autor: michel
# data 13/03/2024

vogal = lambda caractere: caractere.lower() in "aeiou"

caractere = "a"
print(vogal(caractere)) # True

# exemplo de uso 1
if vogal(caractere):
    print(f"{caractere} é uma vogal")
else:
    print(f"{caractere} não é uma vogal") # a é uma vogal

# exemplo de uso 2
if caractere in "aeiou":
    print(f"{caractere} é uma vogal")
else:
    print(f"{caractere} não é uma vogal")