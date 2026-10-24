#ESTRUCTURA IF-ELSE
#Es una estructura condicionalque permite que un
#programa elija que instrucciones ejecutar
#dependiendo de si una condicional se cumpla o no

#Una condición es una expresión que Python
#evualua como Verdadera (True) o falsa (False)

#operadores de comparación
""" 
== Igual a 
!= Distinto de 
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que
"""

#ESTRUCTURAS
""" if (condicion)
    instruciones_si_verdadero

else:
    instrucciones_si_falso
 """

#ESTRUCTURA IF ELSE Y ELIF
""" 
if (Condicion):
    instrucciones_si_verdadero

elif (condicion_2):
    instrucciones_si_verdadero_2
else:
    instrucciones_si_falso    
"""

#EJEMPLOS
#1 Positivo, negativo o cero 
""" numero = int(input("Ingresar un número: "))  """

#Condicional

""" if (numero > 0):
    print("POSITIVO") 

elif (numero == 0):
    print("Tu número es cero")

else:
    print("NEGATIVO")  """

#PAR O IMPAR
""" numero = int(input("Ingresar un número: "))

if (numero % 2 == 0): 
    print("PAR")

else:
    print("IMPAR") 
 """

#Persona es mayor de edad

""" edad = int(input("Ingresa una edad: ")) 
if (edad >= 18):
    print("Mayor de edad") 

else:
    print("Menor de edad") 

 """

#MAYOR DE DOS NÚMEROS
""" numero_1 = int(input("Ingresa el primer número: ")) 
numero_2 = int(input("Ingresa el segundo número: ")) 

if (numero_1 > numero_2): 
    print("Es mayor el: ", numero_1) 

elif (numero_2 > numero_1): 
    print("El mayor es: ", numero_2)

else:
    print("Los números son iguales")  """

#Clasificar una calificación
#La calificación debe estar entre 0 y 10
#Si es mayor o igual a 9 -> "Excelente"
#Si es mayor o igual a 8 -> "Muy bien"
#Si es mayor o igual a 6 -> "Aprobado" 
#Si es menor a 6 -> "Reprobado"

""" calificacion = float(input("Ingresa la calificación: ")) 
if (calificacion < 0 or calificacion > 10): 
    print("Calificación inválida")
elif (calificacion >= 9):
    print("Excelente") 
elif (calificacion >= 8):
    print("Muy bien")
elif (calificacion >= 6):
    print("Aprobado")
else :
    print("Reprobado") """

#Descuento de una compra
#Si el monto total es mayor o igual a 1000 aplicar descuento del 10%
#Si es menor de 1000 hacer cobro normal

""" compra = float(input("Ingresa el total de la compra: ")) 
if (compra >= 1000):
    descuento = compra * .1
    total = compra - descuento
    print("El total final es: ", total)
else:
    print("El total es: ", compra)  """

#Acceso con 2 requisitos
#Solicitar edad e identificación
#and -> ("Y") Ambas condiciones se cumplen
#or -> ("O") Solo una condición se cumple
""" edad = int(input("Ingresa tu edad: ")) 
identificacion = input("¿Tiene identificación?: ")  """

#SI, si, Si, sI
#Transformar a minusculas
""" respuesta = identificacion.lower()

if edad >= 18 and respuesta=="sí":
    print("Acceso permitido") 

elif edad >= 18 and respuesta=="si":
    print("Acceso permitido") 

else:
    print("Acceso denegado")  """


#Condicion anida
#usuario: admin
#Contraseña: admin123
usuario = input("Usuario: ") 
contrasena = input("Contraseña: ") 

if usuario == "admin":
    print("Usuario correcto") 
    if (contrasena == "admin123"):
        print("Bienvenido") 
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario incorrecto") 