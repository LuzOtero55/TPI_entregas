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
    return print(agua, "ltrs de agua")


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


print("BIENVENIDOS A SOLIDO SIMULATOOOOOOOOOR (Suena musica epica)")

# Paso 1: Calcular el volumen V = l * a * e
print("Calcularemos el volumen de cemento a llenar, para eso complete con las dimensiones")
longitud = float(input("Ingrese la longitud: "))
ancho = float(input("Ingrese el ancho: "))
espesor = float(input("Ingrese el espesor: "))
volumen = longitud * ancho * espesor
print("El volumen es: ", round(volumen, 2), "m3 \n")

# Paso 2: Dosificacion del concreto
print("Seleccione la dosificacion de concreto que necesita: ")
dosificacion = int(input("1) Tipo 1:2:2 (3500Psi / Resistencia 246Kg/cm2)\n"
                         "2) Tipo 1:2:3 (3000Psi / Resistencia 210Kg/cm2)\n"
                         "3) Tipo 1:2:4 (2500Psi / Resistencia 175Kg/cm2)\n"
                         "4) Tipo 1:3:4 (2000Psi / Resistencia 140Kg/cm2)\n"
                         "5) Tipo 1:3:6 (1500Psi / Resistencia 105Kg/cm2)\n"))

while dosificacion > 5 or dosificacion < 1:
    print("Error! La opcion seleccionada es inválida, vuelva a ingresarla: ")
    dosificacion = int(input())

print("\nPara llenar", round(volumen, 2), "m3 de cemento se necesitaran: ")
kilos_cemento(dosificacion)
cantidad_agua(dosificacion)
volumen_grava(dosificacion)
volumen_arena(dosificacion)

print("\n\nMuchas gracias por usar Solido Simulator!\nSolido Simulator © - 2023")
