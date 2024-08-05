import actividad1
import actividad2
while True:
    opcion = input("Ingresa la opcion: ")
    if opcion == "1":
        actividad1.decisionSimple()
    if opcion == "2":
        actividad2.decisionAnidada()
    else:
        print("error")

