
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print ("es menor")

    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

nota = float(input("ingrese su nota: "))

if nota >= 6:
    print("APROBADO")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

nro = int(input("ingrese un numero: "))

if (nro % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input(" ingrese su edad: "))

if edad <12:
    print("Niño/a.")
elif edad >=12 and edad < 18:
    print("adolescente")
elif edad >=18 and edad < 30:
    print("Adulto/a joven")
else:
    print("adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

contraseña = input("ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean 
import random

LNA = [random.randint(1, 100) for i in range(50)]  #LNA = lista numeros aleatorios

mode = float(mode(LNA))
mean = float(mean(LNA))
median = float(median(LNA))

if ( (mean > median) and (median > mode)):
    print("sesgo positivo")
elif ( (mean < median) and (median < mode)):
    print("sesgo negativo")
elif (mean == median == mode):
    print("sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

cadena = input("ingrese una frase o palabra:  ")
UC = cadena[-1] #UC = ultimo caracter

if ((UC == 'a') or (UC == 'e') or (UC == 'i') or (UC == 'o') or (UC == 'u')):
    print(cadena,"!")
else:
    print(cadena)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla

nombre = input(" ingrese su nombre:")

print("seleccione una de las siguientes opciones:")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula")

op = int(input("opcion: "))

if(op == 1):
    mayusc = nombre.upper()
    print(f"{mayusc}")
elif(op == 2):
    minusc = nombre.lower()
    print(minusc)
elif(op == 3):
    PLM =nombre.title()
    print(PLM)
 

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

mag = float(input ("ingrese la magnitud del terremoto: "))

if mag < 3:
    print("Muy leve (imperceptible).")
elif mag <= 3 and mag < 4:
    print("Leve (ligeramente perceptible). ")
elif mag <= 4 and mag < 5:  
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif mag <= 5 and mag < 6:
    print("Fuerte (puede causar daños en estructuras débiles). ")
elif mag <= 6 and mag <7:
    print("Muy Fuerte (puede causar daños significativos).")
elif mag >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
               
