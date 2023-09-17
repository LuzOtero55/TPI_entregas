# Calcular el volumen: V= L * a * e

def calculo_volumen():
    longitud= int(input("Ingrese la longitud: "))
    ancho=int(input("Ingrese el ancho: "))
    espesor= float(input("Ingrese el espesor: "))
    global volumen
    volumen = longitud * ancho * espesor
    return print("El volumen es:",round(volumen,2), "m3")

calculo_volumen()

#paso 2: dosificacion del concreto
#A modo de Ejemplo:
print("Para una dosificacion 1:2:3 - Un concreto con resistencia de 3000psi(lib/ pulg) o 210 (Kg/cm2)")
print("tenemos cemento igual a 350kg, arena 0.56m3, grava 0,84m3 y agua 180L equivale; a 1m3 de concreto")

#Calculo con bolsas de 50kg y desperdicio aprox del 5%
def bolsas_cemento():
    cantidadbolsas= int(7)
    resultado= volumen * cantidadbolsas * float(1.05)
    return print("La cantidad de sacos de 50kg a utilizar son:", round(resultado,2))
bolsas_cemento()

def volumen_arena():
    resultado=volumen * float(0.56)
    return print("El volumen de arena es:", round(resultado,2),"m3")

volumen_arena()

def volumen_grava():
    resultado=volumen * float(0.84)
    return print("El volumen de grava es:", round(resultado,2),"m3")
volumen_grava()

def cantidad_agua():
    resultado=volumen * int(180)
    return print("La cantidad de agua necesaria es:", resultado,"L/m3")
cantidad_agua()




