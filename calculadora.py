while True:
    print("¿Que operación desea realizar?")
    print("Seleccione una opción")
    print("1-SUMAR")
    print("2-RESTAR")
    print("3-MULTIPLICAR")
    print("4-DIVIDIR")
    print("CAAMBIO DEL PROGRAMA INICIAL")
    x= input("Escribe tu elección")
    y=float(x)

    if(y==1):
        a=input("introduce el primer numero\n")
        b=input("Introduce el segundo numero\n")
        a2=float(a)
        b2=float(b)
        resultado= a2+b2
        print("El resultado es: ",resultado)
        print(f"{a} + {b} = {a2+b2}")
    elif(y==2):
        a=input("introduce el primer numero\n")
        b=input("Introduce el segundo numero\n")
        a2=float(a)
        b2=float(b)
        resultado= a2-b2
        print("El resultado es: ",resultado)
        print(f"{a} - {b} = {a2-b2}")
    elif(y==3):
        a=input("introduce el primer numero\n")
        b=input("Introduce el segundo numero\n")
        a2=float(a)
        b2=float(b)
        resultado= a2*b2
        print("El resultado es: ",resultado)
        print(f"{a} x {b} = {a2*b2}")
    elif(y==4):
        a=input("introduce el primer numero\n")
        b=input("Introduce el segundo numero\n")
        a2=float(a)
        b2=float(b)
        resultado= a2/b2
        print("El resultado es: ",resultado)
        print(f"{a} : {b} = {a2/b2}")
        print()

        
        print("¿Desea realizar otra operación?")
        print("Seleccione una opción")
        print("1. Si deseo otra operación")
        print("2. No, quiero salir")
        opcion = input("ingrese su opción: ")

        if opcion == "1":
            print("Reiniciando programa")
        elif opcion == "2":
            print("Saliendo del programa")
            break
        else:
            print("opción no válida. Por favor seleccione opción 1 o 2.")






































 

















































