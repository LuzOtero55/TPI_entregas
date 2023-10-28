# Funciones utilizadas
def kilos_cemento(d):
    cemento = 0
    match d:
        case 1:
            cemento = 8.4
        case 2:
            cemento = 7
        case 3:
            cemento = 6
        case 4:
            cemento = 5.2
        case 5:
            cemento = 4.2
    cemento = (volumen * cemento) * 1.05
    return print(round(cemento, 2), "bolsas de 50kg de cemento")


def cantidad_agua(d):
    agua = 0
    match d:
        case 1:
            agua = 220
        case 2:
            agua = 180
        case 3:
            agua = 170
        case 4:
            agua = 170
        case 5:
            agua = 160
    agua = volumen * agua
    return print(agua, "litros de agua")


def volumen_grava(d):
    grava = 0
    match d:
        case 1:
            grava = 0.67
        case 2:
            grava = 0.84
        case 3:
            grava = 0.96
        case 4:
            grava = 0.84
        case 5:
            grava = 1
    grava = volumen * grava
    return print(round(grava, 2), "m3 de grava")


def volumen_arena(d):
    arena = 0
    match d:
        case 1:
            arena = 0.67
        case 2:
            arena = 0.56
        case 3:
            arena = 0.48
        case 4:
            arena = 0.63
        case 5:
            arena = 0.5
    arena = volumen * arena
    return print(round(arena, 2), "m3 de arena")


print("BIENVENIDOS A SOLIDO SIMULATOR!")

# Paso 1: Ingreso y calculo del volumen
print("Calcularemos el volumen de cemento necesario, para ello complete con las dimensiones")
longitud = float(input("Ingrese la longitud de la estructura: "))
while longitud <= 0:
    print("Error! El dato ingresado es invalido, ingrese la longitud nuevamente: ")
    longitud = float(input())
ancho = float(input("Ingrese el ancho de la estructura: "))
while ancho <= 0:
    print("Error! El dato ingresado es invalido, ingrese el ancho nuevamente: ")
    ancho = float(input())
espesor = float(input("Ingrese el espesor de la estructura: "))
while espesor <= 0:
    print("Error! El dato ingresado es invalido, ingrese el espesor nuevamente: ")
    espesor = float(input())
volumen = longitud * ancho * espesor
print("El volumen es: ", round(volumen, 2), "m3 \n")

# Paso 2: Selecciona la dosificación del concreto
print("Seleccione la dosificación de concreto que necesita: ")
dosificacion = int(input("1) Tipo 1:2:2 (3500Psi / Resistencia 246Kg/cm2)\n"
                         "2) Tipo 1:2:3 (3000Psi / Resistencia 210Kg/cm2)\n"
                         "3) Tipo 1:2:4 (2500Psi / Resistencia 175Kg/cm2)\n"
                         "4) Tipo 1:3:4 (2000Psi / Resistencia 140Kg/cm2)\n"
                         "5) Tipo 1:3:6 (1500Psi / Resistencia 105Kg/cm2)\n"))

while dosificacion > 5 or dosificacion < 1:
    print("Error! La opción seleccionada es inválida, vuelva a ingresarla: ")
    dosificacion = int(input())

# Paso 3: Imprime los resultados
print("\nPara llenar", round(volumen, 2), "m3 de cemento se necesitan: ")
kilos_cemento(dosificacion)
cantidad_agua(dosificacion)
volumen_grava(dosificacion)
volumen_arena(dosificacion)

print("\n\nMuchas gracias por utilizar Solido Simulator!\nSolido Simulator © - 2023")
