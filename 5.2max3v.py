while True:
    try:
        #Pedimos al usuario los valores
        v1 = int(input('ingrese un numero:'))
        v2 = int(input('ingrese un segundo:'))
        v3 = int(input('ingrese un tercer:'))
        break;
    except ValueError:
        #Esto es para evitar que escriba letras
        print("Debes escribir solo números.")
    continue

#Averiguamos cual es el maximo y lo mostramos
def Maximo(v1,v2,v3):
    print("-----------------------")
    if (v1 > v2) & (v1 > v3):
        print ('El valor maximo es',v1)
    elif v2 > v3:
        print ('El valor maximo es',v2)
    else:
        print ('El valor maximo es',v3)

Maximo(v1,v2,v3);
