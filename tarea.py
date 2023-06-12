# 1 -Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no , mostrando un mensaje.
'''''
print("se compararan dos caracteres")
letra1 = input("ingrese una letra")
letra2 = input("ingrese una letra")

if letra1 == letra2 :
    print("las dos letras son iguales!")

else:
    print("las letras no son iguales!")
'''

#2 -Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla
"""""
print("se compararan dos frases")
palabra1 = input("ingrese una frase")
palabra2 = input("ingrese la segunda frase")

if palabra1 == palabra2:
    print("las palabras son iguales")

else:
    print("no son iguales")
"""

#3 -Realizar un programa que permita ingresar "f" o "m" y determinar si vota en mesa femenina o masculina
"""""
genero = input("ingrese su genero f o m :")

if genero == "f" or genero == "F":
    print("votas en mesa femenina!")
elif genero == "m" or genero == "M":
    print("votas en mesa masculina!")
else:
    print("No es valido! por favor ingrese f o m!")
"""

#4 -Realice un programa que lea dos numeros y diga cual es el mayor.
"""""
num1 = int(input("Ingrese un numero :"))
num2 = int(input("Ingrese un numero :"))

if num1 == num2:
    print("son iguales")

else:
    print("no son iguales!")
"""

#5 - Realice un programa que cambie pesos a dolares. mejorelo , añadiendo el cambio de dolares a peso y que sea el usuario quien decida que tipo de cambio quiere , si de dolares a pesos o viceversa.
"""""
print("¡Bienvenido al convertidor de moneda!")

opcion = input("Seleccione una opción:\n 1. Pesos a Dólares\n 2. Dólares a Pesos\n")

if opcion == '1':
    cantidad_pesos = float(input("Ingrese la cantidad de pesos: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    resultado = cantidad_pesos / tipo_cambio
    print(f"{cantidad_pesos} pesos equivale a {resultado} dólares.")
elif opcion == '2':
    cantidad_dolares = float(input("Ingrese la cantidad de dólares: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio: "))
    resultado = cantidad_dolares * tipo_cambio
    print(f"{cantidad_dolares} dólares equivale a {resultado} pesos.")
else:
    print("Opción inválida. Por favor, seleccione 1 o 2.")
"""
# 6 - Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años,muestre un mensaje diciendo "puedes votar" , si no "no puede votar".
""""
Edad = int(input("Ingrese su edad :"))

if Edad <= 16 :
    print("no puede votar")

else:
    print("puede votar") 
"""

#EJERCICIOS ESTRUCTURA CONDICIONAL COMPUESTO (IF ANIDADOS)

# 1 -Introducir los lados de un triangulo y visualizar por pantalla si dicho triangulo es equilatero ,isosceles o escaleno
""""
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("Es un triángulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")
"""
# 2 -Realice un programa que le permita al usuario simular el pago ingresado el importe y la forma de pago: contador (1):se aplica un descuento del 10% al importe , Tarjeta (2): se aplica un interes de 10% ,debito (3): se aplica un descuento del 5% , mostrar el importe , el descuento o interes y el importe total.
"""
importe = float(input("Ingrese el importe a pagar: "))
forma_pago = int(input("Seleccione la forma de pago:\n 1. Contador\n 2. Tarjeta\n 3. Débito\n"))

descuento = 0
interes = 0

if forma_pago == 1:
    descuento = importe * 0.1
elif forma_pago == 2:
    interes = importe * 0.1
elif forma_pago == 3:
    descuento = importe * 0.05

importe_total = importe - descuento + interes

print("Importe: $", importe)
print("Descuento: $", descuento)
print("Interés: $", interes)
print("Importe total a pagar: $", importe_total)
"""

# 3 -Realice un programa que lea tres numeros,muestre cual es el mayor y determine si es par o impar
""""
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

mayor = max(numero1, numero2, numero3)
print("El número mayor es:", mayor)

if mayor % 2 == 0:
    print("El número mayor es par.")
else:
    print("El número mayor es impar.")
"""

# 4 -confeccione un programa que pida un numero del 1 al 7 y diga el dia de la semana correspondiente.
""""
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    dia_semana = "Lunes"
elif numero == 2:
    dia_semana = "Martes"
elif numero == 3:
    dia_semana = "Miércoles"
elif numero == 4:
    dia_semana = "Jueves"
elif numero == 5:
    dia_semana = "Viernes"
elif numero == 6:
    dia_semana = "Sábado"
elif numero == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Número inválido. Ingrese un número del 1 al 7."

print("El día de la semana correspondiente es:", dia_semana)
"""

# 5 -Realice un programa que pida un numero del 1 al 12 y diga el nombre del mes correspondiente
"""""
numero = int(input("Ingrese un número del 1 al 12: "))

if numero == 1:
    mes = "Enero"
elif numero == 2:
    mes = "Febrero"
elif numero == 3:
    mes = "Marzo"
elif numero == 4:
    mes = "Abril"
elif numero == 5:
    mes = "Mayo"
elif numero == 6:
    mes = "Junio"
elif numero == 7:
    mes = "Julio"
elif numero == 8:
    mes = "Agosto"
elif numero == 9:
    mes = "Septiembre"
elif numero == 10:
    mes = "Octubre"
elif numero == 11:
    mes = "Noviembre"
elif numero == 12:
    mes = "Diciembre"
else:
    mes = "Número inválido. Ingrese un número del 1 al 12."

print("El nombre del mes correspondiente es:", mes)
"""