#ESTRUCTURA IF-ELSE 
#Es una estructura condicional que permite que un programa elija qué instrucciones ejecutar 
#dependiendo de si una condición se cumple o no

#una condición es una expresión que Python evalua como
#Verdadera (True) o Falsa (False)


#Operadores de Comparación
""" 
== Igual a
!= Distinto de
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que 
 """

#ESTRUCTURA
"""
if (condición):
    instrucciones_si_verdadero
else:
    instrucciones_si_falso
"""


#ESTRUCTURA IF ELSE y ELIF
"""
if (condicion):
    instrucciones_si_verdadero

elif (condicion_2):
    instrucciones_si_verdadero_2
else:
    instrucciones_si_falso
"""

#EJEMPLO 1 - positivo negativo o cero
""" numero = int(input("Ingresa un número: "))
#condicional
if (numero > 0):
    print("Positivo")

elif (numero == 0):
    print("Tu número es cero")

else:
    print("Negativo")
 """


#Par o Impar
""" numero = int(input("Ingresa un número: "))

if (numero % 2 ==0):
    print("PAR")

else:
    print("IMPAR") """


#Persona es Mayor de Edad
""" edad = int(input("Ingresa la edad: "))

if (edad >= 18):
    print("Mayor de Edad")

else:
    print("Menor de Edad")
 """


#Mayor de dos números
""" numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))

if (numero_1 > numero_2):
    print("Es mayor el: ", numero_1)

elif (numero_2 > numero_1):
    print("El mayor es: ", numero_2)

else:
    print("Los numeros son iguales") """


#Calsificar una calificación
#La calificación debe estar entre 0 y 10
#Si es mayor o igual a 9 "Excelente"
#Si es mayor o igal a 8 "Muy bien"
#Si es mayor o igual a 6 "Aprobado"
#Si es menor a 6 "Reprobado"

""" calificacion = float(input("Ingresa la calificación: "))

if (calificacion < 0 or calificacion > 10):
    print("Calificación Inválida")

elif (calificacion >= 9):
    print("Excelente")

elif (calificacion >= 8):
    print("Muy bien")

elif (calificacion >= 6):
    print("Aprobado")

else:
    print("Reprobado")
 """

#Descuento de una compra
#Si el monto total es ayor a 1000 aplicar descuento del 10%
#Si es menor de $1000 hacer cobro normal

""" total_compra = float(input("Ingresa el total: "))

if (total_compra >= 1000):
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print("El total final es: ", total_final)

else:
    print("El total es: $ ", total_compra)
"""


#Acceso con 2 requisitos
#Solicitar edad e identificación
#and -> ("Y") Ambas condiciones se cumplen
#or -> ("O") Solo una condición se cumple

""" edad = int(input("Ingresa tu edad: "))
identificacion = input("¿Tienes identificación?: ")

#SI, si, Si, sI
#Transformar a minúsculas
respuesta = identificacion.lower()

if edad >= 18 and respuesta =="si":
    print("Acceso permitido")

else:
    print("Acceso denegado")
"""



#Condicion Anidada 
#usuario: admin
#contraseña: admin123
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin":
    print("Usuario Correcto")
    if (contrasena == "admin123"):
        print("Bienvenido")
    else:
        print("Contraseña Incorrecta")
else: 
    print("Usuario incorrecto")




