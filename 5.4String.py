import os

String = input("Ingrese un string:")
characters = len(String)

def centrado(Str, chts):
    size = os.get_terminal_size().columns - chts;
    print(Str.center(size))
    print('Caracteres necesarios para centrarse:' ,size)


centrado(String, characters)