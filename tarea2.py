# EJERCICIOS ESTRUCTURAS REPETITIVAS Y ESTRUCTURAS CONDICIONALES

# 1 - Realice un programa que lea 4 numeros y diga cuantos son pares y cuantos impares y devuelva la sumatoria de los pares
"""""
numeros = []

for i in range(4):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
suma_pares = sum(pares)

print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))
print("Suma de los números pares:", suma_pares)
"""

# 2 -Leer 10 numeros y obtener la cantidad de mayores y la cantidad de menores a 100,cual es el numero maximo y cual es el numero minimo.
"""""
numeros = []
mayores_100 = 0
menores_100 = 0

for i in range(10):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

    if num > 100:
        mayores_100 += 1
    elif num < 100:
        menores_100 += 1

numero_maximo = max(numeros)
numero_minimo = min(numeros)

print("Cantidad de números mayores a 100:", mayores_100)
print("Cantidad de números menores a 100:", menores_100)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)
"""

# 3-Ingresa las edades y el sexo de 15 personas y determinar cuantas son mujeres , cuantos varones , cuantos mayores de edad y cuantos menores de edad.
""""
mujeres = 0
varones = 0
mayores_edad = 0
menores_edad = 0

for i in range(15):
    print(f"\nPersona {i+1}:")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ")

    if sexo == "M" or sexo == "m":
        varones += 1
    elif sexo == "F" or sexo == "f":
        mujeres += 1

    if edad >= 18:
        mayores_edad += 1
    else:
        menores_edad += 1

print("\nResultados:")
print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de mayores de edad:", mayores_edad)
print("Cantidad de menores de edad:", menores_edad)
"""

# 4 - Leer 10 numeros y mostrar solamente los numeros positivos y su sumatoria
""""
numeros = []
sumatoria = 0

for i in range(10):
    num = float(input("Ingrese un número: "))
    numeros.append(num)

    if num > 0:
        sumatoria += num

numeros_positivos = [num for num in numeros if num > 0]

print("Números positivos:", numeros_positivos)
print("Sumatoria de los números positivos:", sumatoria)
"""

# 5 - Leer 15 numeros negativos y convertirlos a positivos e imprimir dichos numeros.
""""
numeros_positivos = []

for i in range(15):
    num = float(input("Ingrese un número negativo: "))
    num_positivo = abs(num)  # Utilizamos la función abs() para obtener el valor absoluto
    numeros_positivos.append(num_positivo)

print("Números convertidos a positivos:")
for num in numeros_positivos:
    print(num)
"""
