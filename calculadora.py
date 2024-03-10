def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    else:
        return num1 / num2

def calculadora():
    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("\nIngrese el número de la operación deseada: ")

        if opcion == '5':
            print("Saliendo de la calculadora...")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("El resultado de la suma es:", suma(num1, num2))
        elif opcion == '2':
            print("El resultado de la resta es:", resta(num1, num2))
        elif opcion == '3':
            print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
        elif opcion == '4':
            print("El resultado de la división es:", division(num1, num2))
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


calculadora()