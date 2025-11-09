""" 
1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    return "Hola Mundo!"

#            MAIN:

print(imprimir_hola_mundo())

------------------------------------------------------------------------------------------------------------
 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un 
 saludo personalizado.
 Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”.
 Llamar a esta función desde el programa principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#            MAIN:

NombreUsuario = input("Ingrese su nombre: ")

saludar_usuario(NombreUsuario)

------------------------------------------------------------------------------------------------------------
3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro 
parámetros e imprima: 
“Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
Pedir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#            MAIN:

Nombre   = input ("¿cual es su nombre? ")
Apellido = input ("¿y su apellido? ")
Edad     = input ("ingrese su edad: ")
Locacion = input ("¿donde vivis? ")

informacion_personal(Nombre,Apellido,Edad,Locacion)

-------------------------------------------------------------------------------------------------------------
 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el 
 área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el 
 perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(r: float) -> float:
    
    A = round(math.pi * math.pow(r,2),3)
    
    return A

def calcular_perimetro_circulo(r):
    
    P = round(2 * math.pi * r, 3)

    return P

#           MAIN

radio = float(input("ingrese el radio del circulo: R = "))

print(f"el area del circulo es: {calcular_area_circulo(radio)}"
      f" y su perimetro es: {calcular_perimetro_circulo(radio)}")

"""