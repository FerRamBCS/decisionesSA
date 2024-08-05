def decisionAnidada():
    # Solicitar al usuario que ingrese su edad e ingresos
    edad = int(input("Por favor, ingrese su edad: "))
    ingresos = float(input("Por favor, ingrese sus ingresos mensuales: "))

    # Estructura de decisión anidada
    if edad >= 18:
        if ingresos >= 30000:
            print("Eres elegible para un préstamo.")
        else:
            print("No eres elegible para un préstamo debido a tus ingresos bajos.")
    else:
        print("No eres elegible para un préstamo debido a tu edad.")

