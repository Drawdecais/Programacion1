#!/usr/bin/python3
#Declaro una tupla de un solo elemento
Datos = ('lista de las edades de una población que ha ido a vacunarse',)
#Compruebo que detecte un solo elemento
print("Cantidad de elementos de la tupla 'Datos' es:", len(Datos))

print("Edades de una población que ha ido a vacunarse:")
#Declaro la lista de edades
vEdades = [2, 7, 58, 7, 45, 26, 10, 8, 56, 57, 97, 19, 11, 53, 3, 99, 62, 78, 29, 9, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 10, 58, 512, 24, 92, 89, 67, 53, 10, 9, 83, 1, 44, 10, 77, 98, 73, 57]
#Muestro en pantalla la lista con un ciclo for
for vEdad in vEdades:
    #Elimino de la lista el numero 10
    if vEdad == 10:
        vEdades.remove(10)
    #Imprimir en pantalla la lista
    print("edad:", vEdad, "años")

Total = len(vEdades)
print("ToTal:", Total + 1)