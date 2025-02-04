#CONTRASEÑA

import random

# Lista de palabras para la passphrase
palabras = ["sol", "luna", "mar", "montaña", "rojo", "azul", "perro", "gato"]

def generar_contraseña(longitud):
    """Genera una contraseña aleatoria con letras y números."""
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(random.choice(caracteres) for _ in range(longitud))

def generar_frase(num_palabras=4):
    """Genera una frase usando palabras aleatorias."""
    return "-".join(random.choice(palabras) for _ in range(num_palabras))


opcion = input("Seleccione el tipo de contraseña (1: Contraseña aleatoria, 2: frase): ")

if opcion == "1":
    longitud = int(input("Ingrese el tamaño de la contraseña: "))
    print("La contraseña generada es:", generar_contraseña(longitud))
elif opcion == "2":
    num_palabras = int(input("Ingrese el número de palabras para la frase: "))
    print("La passphrase generada es:", generar_frase(num_palabras))
else:
    print("Opción no válida.")