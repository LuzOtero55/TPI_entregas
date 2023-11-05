import sys
import os


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
    cemento = round(cemento, 2)
    return cemento


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
    return agua


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
    grava = round(grava, 2)
    return grava


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
    arena = round(arena, 2)
    return arena


def menu():
    limpieza = ''
    if os.name == "posix":
        limpieza = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        limpieza = "cls"
    os.system(limpieza)
    print("")
    print("-" * 31)
    print("BIENVENIDOS A SOLIDO SIMULATOR!")
    print("-" * 31)
    print("")
    print("Que operacion desea realizar?")
    print("1) Ingresar como cliente")
    print("2) Registrarse como cliente")
    print("3) Eliminar un cliente")
    print("4) Salir")
    print("")
    while True:
        try:
            opcion = int(input("Ingrese la opcion deseada: "))
            if opcion not in (1, 2, 3, 4):
                raise SyntaxError("Opcion invalida!")
            else:
                return int(opcion)
        except (ValueError, SyntaxError) as error:
            print(f"Error! {error}")
        else:
            break


def ingreso_cliente(file, dni):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return input("El fichero " + file + " no existe.\n")
    else:
        direccion = f.readlines()
        f.close()
        for line in direccion:
            clientes = line.split(": ")
            if clientes[0] == dni:
                apellido, nombre, telefono = clientes[1].split(", ")
                print("\n", "-" * 31, f"\n\nBienvenido {apellido} {nombre}!\nDNI: {dni} - Tel: {telefono}\n")
                print("En que tipo de unidad de medida te gustaria trabajar?: ")
                print("1) Metros")
                print("2) Pies")
                print("3) Centímetros\n")
                while True:
                    try:
                        unidad = int(input("Ingrese la opcion de la unidad deseada: "))
                        if unidad not in (1, 2, 3):
                            raise SyntaxError("Opcion invalida!")
                        else:
                            break
                    except (ValueError, SyntaxError) as error:
                        print(f"Error! {error}")
                calc_volumen(unidad)
                dosif_concreto(dni, apellido, nombre, telefono)
                break
        else:
            return input("El cliente N°" + dni + " no existe.\n")


def registrar_cliente(file):
    while True:
        try:
            dni = int(input("\nIngrese su N° de DNI: "))
            if dni < 0:
                raise SyntaxError("El dni ingresado es invalido.")
            apellido = input("Ingrese su apellido: ")
            if ',' in apellido or ':' in apellido:
                raise SyntaxError("Esta usando caracteres invalidos.")
            nombre = input("Ingrese su nombre: ")
            if ',' in nombre or ':' in nombre:
                raise SyntaxError("Esta usando caracteres invalidos.")
            telefono = int(input("Ingrese su N° de telefono: "))
            if telefono < 0:
                raise SyntaxError("El telefono ingresado es invalido.")
        except (ValueError, SyntaxError) as error:
            print(f"Error! {error}")
        else:
            break
    try:
        f = open(file, 'a')
    except FileNotFoundError:
        return print("El fichero " + file + " no existe.\n")
    else:
        f.write(f"{str(dni)}: {apellido}, {nombre}, {str(telefono)}\n")
        f.close()
    return input("El cliente a sido agregado con exito!")


def eliminar_cliente(file):
    dni = input("\nIngrese su N° de DNI: ")
    clientes = []
    cliente_elimado = False
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return input("El fichero " + file + " no existe.\n")
    else:
        direccion = f.readlines()
        f.close()
        for line in direccion:
            direccion = line.split(": ")
            if direccion[0] == dni:
                cliente_elimado = True
            else:
                clientes.append(line)
        if cliente_elimado:
            f = open(file, 'w')
            f.writelines(clientes)
            return input(f"El cliente N°{dni} ha sido eliminado con exito!")
        else:
            return input(f"El cliente N°{dni} no existe.\n")


volumen = 0
uni = ''


def calc_volumen(unidad):
    print("\nCalcularemos el volumen de cemento necesario, para ello complete con las dimensiones")
    longitud = float(input("\nIngrese la longitud de la estructura: "))
    while longitud <= 0:
        print("Error! El dato ingresado es invalido, ingrese la longitud nuevamente: ")
        longitud = float(input())
    ancho = float(input("\nIngrese el ancho de la estructura: "))
    while ancho <= 0:
        print("Error! El dato ingresado es invalido, ingrese el ancho nuevamente: ")
        ancho = float(input())
    espesor = float(input("\nIngrese el espesor de la estructura: "))
    while espesor <= 0:
        print("Error! El dato ingresado es invalido, ingrese el espesor nuevamente: ")
        espesor = float(input())
        global volumen
        global uni
    volumen = longitud * ancho * espesor
    match unidad:
        case 1:
            print("\n\nEl volumen es: ", round(volumen, 2), "m3 \n\n")
            uni = 'm3'
        case 2:
            print("\n\nEl volumen es: ", round(volumen, 2), "ft3 \n\n")
            volumen = volumen/35.315
            uni = 'ft3'
        case 3:
            print("\n\nEl volumen es: ", round(volumen, 2), "cm3 \n\n")
            volumen = volumen / 1000000
            uni = 'cm3'


def dosif_concreto(dni, apellido, nombre, telefono):
    print("Tipos de dosificacion de concreto: ")
    print("1) Tipo 1:2:2 (3500Psi / Resistencia 246Kg/cm2)\n"
          "2) Tipo 1:2:3 (3000Psi / Resistencia 210Kg/cm2)\n"
          "3) Tipo 1:2:4 (2500Psi / Resistencia 175Kg/cm2)\n"
          "4) Tipo 1:3:4 (2000Psi / Resistencia 140Kg/cm2)\n"
          "5) Tipo 1:3:6 (1500Psi / Resistencia 105Kg/cm2)\n")
    dosificacion = int(input("Seleccione la dosificación de concreto que necesita: "))

    while dosificacion > 5 or dosificacion < 1:
        print("Error! La opción seleccionada es inválida, vuelva a ingresarla: ")
        dosificacion = int(input())

    print("\nPara llenar", round(volumen, 2), uni, " de cemento se necesitan: ")
    print(f"\n{kilos_cemento(dosificacion)} bolsas de 50kg de cemento")
    print(f"\n{cantidad_agua(dosificacion)} litros de agua")
    print(f"\n{volumen_grava(dosificacion)} m3 de grava")
    print(f"\n{volumen_arena(dosificacion)} m3 de arena\n")
    historial_hormigonera(dni, kilos_cemento(dosificacion), cantidad_agua(dosificacion),
                          volumen_grava(dosificacion), volumen_arena(dosificacion))
    ticketera(dni, apellido, nombre, telefono, kilos_cemento(dosificacion), cantidad_agua(dosificacion),
              volumen_grava(dosificacion), volumen_arena(dosificacion))
    ticket = input("Desea imprimir el ticket? (S/N) ")
    if ticket in ('S', 's', 'Si', 'SI', 'Y', 'y'):
        print("")
        imprimir_ticket()
        input("\n\nTicket impreso! Presione cualquier tecla para volver al menu.")
    else:
        input("\nPresione cualquier tecla para volver al menu.")


def imprimir_ticket():
    limpieza = ''
    if os.name == "posix":
        limpieza = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        limpieza = "cls"
    os.system(limpieza)
    f = open("Ticket.txt", 'r')
    direccion = f.readlines()
    f.close()
    for line in direccion:
        print(line)


def ticketera(dni, apellido, nombre, telefono, cemento, agua, grava, arena):
    f = open("Ticket.txt", "w")
    f.writelines("#" * 40)
    f.writelines(f"\n           SOLIDO SIMULATOR\n")
    f.writelines("#" * 40)
    f.writelines(f"\nCLIENTE: {apellido} {nombre}\nDNI N° {dni}     TEL: {telefono}")
    f.writelines("#" * 40)
    f.writelines(f"\nVOLUMEN DE CONSTRUCCION: {volumen}{uni}\n")
    f.writelines("#" * 40)
    f.writelines(f"\n{cemento} bolsas de 50kg de cemento")
    f.writelines(f"\n{agua} litros de agua")
    f.writelines(f"\n{grava} m3 de grava")
    f.writelines(f"\n{arena} m3 de arena\n")
    f.writelines("#" * 40)
    f.close()


def historial_hormigonera(dni, cemento, agua, grava, arena):
    f = open("Historial.txt", "a")
    f.writelines(f"\nVenta a {dni}: \n   Cemento: {cemento} bolsas de 50kg\n   Agua: {agua} lts\n   "
                 f"Grava: {grava} m3\n   Arena: {arena} m3\n")
    f.close()


def main():
    file = "Clientes.txt"
    while True:
        opcion = menu()
        if opcion == 1:
            dni = input("\nIngrese el DNI del cliente: ")
            ingreso_cliente(file, dni)
        elif opcion == 2:
            registrar_cliente(file)
        elif opcion == 3:
            eliminar_cliente(file)
        elif opcion == 4:
            print("\n\nMuchas gracias por utilizar Solido Simulator!\nSolido Simulator © - 2023")
            input()
            sys.exit()
            break


main()
