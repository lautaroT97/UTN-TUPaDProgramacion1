
#ejerciio 1
print ("hola mundo!")


#ejercicio 2:
nombre = input ("ingrese su nombre: ")
print("hola! ",nombre)

#ejeriio 3:
nombre = input ("nombre: ")
apellido = input ("apellido: ")
edad = input ("edad: ")
edad = int(edad)
resid = input("donde residis?: ")

print (F"Soy {nombre} {apellido}, tengo {edad} años y vivo en {resid}")

#ejercicio 4:
import math

radio = input(" ingrese el radio del circulo: ")
radio = float(radio)

A = math.pi * radio**2
P = 2 *math.pi * radio

print(f" el area es {A} y el perimetro es {P}")

#ejercicio 5
sec = input("ingrese un valor ingresado en segundos")
sec = float(sec)

horas = sec / 3600

print(f"{sec}[s] en horas son {horas} [Hs]")

#ejericio 6
nro = input("ingrese un numero")
nro = int(nro)

print (f"0 x {nro} = {0 * nro}")
print (f"1 x {nro} = {1 * nro}")
print (f"2 x {nro} = {2 * nro}")
print (f"3 x {nro} = {3 * nro}")
print (f"4 x {nro} = {4 * nro}")
print (f"5 x {nro} = {5 * nro}")
print (f"6 x {nro} = {6 * nro}")
print (f"7 x {nro} = {7 * nro}")
print (f"8 x {nro} = {8 * nro}")
print (f"9 x {nro} = {9 * nro}")
print (f"10 x{nro} = {10 * nro}")


nro1 = input ("ingrese un nro distinto de 0: ")
nro2 = input ("ingrese un nro distinto de 0: ")

nro1 = int(nro1)
nro2 = int(nro2)

print (f"{nro1} + {nro2} = {nro1 + nro2}")
print (f"{nro1} - {nro2} = {nro1 - nro2}")
print (f"{nro1} * {nro2} = {nro1 * nro2}")
print (f"{nro1} / {nro2} = {nro1 / nro2}")


#ejercicio 8
alt = input("ingrese su altura en metros: ")
peso = input("ingrese su peso en kg: ")

alt = float(alt)
peso = float(peso)

IMC = peso / alt

print(f"el IMC de la persona es {IMC}")


#ejercicio 9
celcius = input ("ingrese la temperatura en grados celcius: ")
celcius = float(celcius)

far = 9 / 5 * celcius + 32

print (f"{celcius}º = {far}[F] ")


#ejercicio 10
n1 = input ("ingrese un nro: ")
n2 = input ("ingrese un nro: ")
n3 = input ("ingrese un nro: ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

prom = (n1 + n2 + n3) / 3

print(f" el promedio de los 3 numeros ingresados es {prom}")
