import math
vPI = math.pi

while True:
    try:
        vRadio = float(input('Ingrece el radio:'))
        break;
    except ValueError:
        print("Solo se admiten números.")
    continue

def valorDelAreal(radio): 
    return print('El area de un circulo con un radio =',radio,' es ',vPI * (radio ** 2));

valorDelAreal(vRadio);
