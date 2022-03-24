#!/usr/bin/python3
from os import remove


Datos = ('lista de las edades de una población que ha ido a vacunarse:')
print(Datos[0:])
vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
vEdades.remove(10)
for vEdad in vEdades:
    print("edad:", vEdad)