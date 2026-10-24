#ESTRUCTURA IF-ELSE
#Es una estructura condicional que permite que un
#programa elija que instrucciones ejecutar
#dependiendo de si una condición se cumple o no

#Una condición es una expresión que Python
#evalua como Verdadera (True) o False (False)

#Operadores de Comparación
""" 
== Igual a
!= Distinto de 
>  Mayor que
<  Menor que
>= Mayor o igual que
<= Menor o igual que """

#ESTRUCTURA IF ELSE y ELIF
""" 
if(condition):
    instrucciones_si_verdadero

elif (condition_2):
    instrucciones_si_verdadero_2


else:
    instrucciones_si_falso """

#EJEMPLOS
""" #1 Positivo, negativo o cero
numero = int(input("Ingresa un número: "))

#condicional
if (numero > 0):
    print("POSITIVO")

elif (numero == 0):
    print("Tu número es cero")

else:
    print("NEGATIVO") """

""" #2 PAR O IMPAR
numero = int(input("Ingresa un número: "))

if (numero % 2 == 0):
    print("PAR")

else:
    print("IMPAR") """

#PERSONA ES MAYOR DE EDAD
""" Edad = int(input("Ingresa tu edad: "))

if(Edad >= 18):
    print("MAYOR DE EDAD")

else:
    print("MENOR DE EDAD") """

#MAYOR DE DOS NÚMEROS
""" numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))

if(numero_1 > numero_2):
    print("Es mayor el: ", numero_1)

elif(numero_2 > numero_1):
    print("El mayor es: ", numero_2)

else:
    print("Los numeros son iguales") """

#CLASIFICAR UNA CALIFICACIÓN
#La calificación debe de estar entre 0 y 10
#Si es mayor o igual a 9 -> "Excelente"
#Si es mayor o igual a 8 -> "Muy bien"
#Si es mayor o igual a 6 -> "Aprobado"
#Si es menor a 6 -> "Reprobado"

""" calificacion = float(input("Ingresa la calificación: "))

if (calificacion < 0 or calificacion > 10 ):
    print("CALIFICACIÓN INVALIDADA")

elif (calificacion >= 9):
    print("EXCELENTE")

elif (calificacion >= 8):
    print("MUY BIEN")

elif (calificacion >= 6):
    print("APROBADO")

else:
    print("REPROBADO") """

#DESCUENTO DE UNA COMPRA
#Si el monto total es mayor o igual a $1000 aplicar descuento del 10%
#Si es menor de $1000 hacer cobro normal
""" total_compra = float(input("Ingresa el total de la compra: "))

if(total_compra >= 1000):
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print("El total final es: ", total_final)

else:
    print("El total es: ", total_compra) """

#ACCESO CON DOS REQUISITOS
#Solicitar edad e identificación
#and -> ("Y") Ambas condiciones se cumplen
#or -> ("O") Solo una condición se cumple
""" edad = int(input("Ingresa tu edad: "))
identificacion = input("¿Tienes identificacion?: ")

#SI, si, Si, sI
#Tranformar a minusculas
respuesta = identificacion.lower()

if edad >=18 and respuesta=="si":
    print("ACCESO PERMITIDO")

else:
    print("ACCESO DENEGADO") """

#CONDICIÓN ANIDADA
#Usuario: admin
#Contraseña: admin123
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin":
    print("USUARIO CORRECTO")
    if(contrasena == "admin123"):
        print("BIENVENIDO")
    else:
        print("CONTRASEÑA INCORRECTA")

else:
    print("USUARIO INCORRECTO")
    
    
