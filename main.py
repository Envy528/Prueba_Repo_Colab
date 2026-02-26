
print("Menú de opciones:")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")
print("5. salir")

m = int(input("Escoge la operación a realizar(1-5): / "))

def menu(m):

    if m == 1:
        print("SUMA")
        print("ADDITION")
        

    elif m == 2:
        print("RESTA")
        print("SUBTRATION")

    elif m == 3:
        print("MULTIPLICACIÓN")
        print("MULTIPLICATION")

    elif m == 4:
        print("DIVISIÓN")
        print("DIVISION")
    
    elif m == 5:
        print("GRACIAS POR TU ATENCIÓN!!")
        print("THANK YOU FOR YOUR TIME!!")

    else:
        print("Opción no valida")
        print("INVALID OPTION")
    return m