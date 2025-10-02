#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for x in range(101):
    print(x)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.numero = input("Por favor, ingresa un número entero: ")
numero = int(input("Por favor, ingresa un número entero: "))
contador = 0
while numero > 0:
    numero //= 10  # División entera
    contador += 1
    
print(f"el numero tiene {contador} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

a = int(input(" ingrese un numero entero: "))
b = int(input(" ingrese un numero entero mayor que el anterior: "))

cont = 0

if a < b:
    for i in range(a,b-1):
        cont = cont + 1
else:
    print("el segundo numero es mayor al primero, intentar nuevamente")

print(f"hay {cont} numeros en el intervalo ({a},{b})")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
i = 0
num = int(input (f"ingrese un numero entero o 0 para finalizar la carga\n num {i+1}: "))
acum = 0

while (num != 0):
    acum = acum + num
    i += 1
    num = int(input (f"ingrese un numero entero o 0 para finalizar la carga\n num {i+1}: "))

print(f"el total acumulado fue: {acum} en una carga total de {i} numeros")


# 5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#from random import randint    //otra forma de importar la libreria
import random
cont = 0

N_aleat = random.randint(0, 9)      #haiendolo con la otra forma quedaria N_aleat = randint(0,9)
#print (N_aleat)

nro = int(input(f"ingrese un numero entero entre el 0 y el 9\nintento nro {cont+1}:"))

while nro != N_aleat:
    cont += 1
    nro = int(input(f"ingrese un numero entero entre el 0 y el 9\nintento nro {cont+1}:"))

print(f"se necesitaron {cont+1} intentos para adivinar el nro {N_aleat}")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for i in range (100,0,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

b = int(input("ingrese un numero entero positivo: "))
sum = 0

for i in range(0,b+1):
    print(f"{i} + {sum} = {sum+i}")
    sum = sum + i
    
print(f"la suma de todos los numeros en el intervalo (0,{b}) es {sum}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

par = 0
impar = 0
neg = 0
pos = 0

print("ingrese numeros enteros")

for i in range (0,10):
    nro = int(input(f"nro {i+1}: "))

    if(nro>0):
        pos += 1
    else:
        neg += 1
    
    if((nro % 2) == 0):
        par += 1
    else:
        impar += 1


print(f"se encontraron {par} numeros pares, {impar} numeros impares,"
      f"{pos} numeros positivos y {neg} numeros negativos")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

acum = 0
cant = 100

print("ingrese numeros enteros")
for i in range (0,cant):
    nro = int(input(f"nro {i+1}: "))
    acum = acum + nro

media =float(acum / cant)

print(f"la media de los {cant} numeros ingresados es: {media}")

    

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

n_invert = 0

nro = int(input("ingrese un numero: "))

while nro > 0:
    digito = nro % 10                # Obtenemos el último dígito
    n_invert = n_invert * 10 + digito   # Construimos el número invertido
    nro //= 10                       # Eliminamos el último dígito del número original

print(n_invert)


