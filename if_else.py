""" """ """ # ESTRUCTURA IF-ELESE 
# Es una estructura condicional que permite que un 
# programa elija que instrucciones ejecutar 
# dependiendo de si una condición se cumple o no 

# Una condición es una exprecion en Python 
# Evalua como Verdadera (True) o False (False) 

# Operadores de Comparacion
  
== Igual a
¡ = Distinto de 
> Mayor que 
<Menor que 
>= Mayor o igual que 
<= Menor o igual que


#ESTRUCTURA

if (condicion)
   instruciones_si_verdadero

else:
   instrucciones_si_falso


   #ESTRUCTURA IF ELSE y ELIF

   if (condicion):
         instruciones_si_verdadero

   elif (condicion_2):
         instruciones_si_verdadero_2

    else:
        istrucciones_si_falso """
        
""" #EJEMPLOS 
#1 Positivo, negativo o cero
numero = int(input("Ingresa un número: "))

#conficional
if (numero > 0):
     print ("POSITIVO")

elif (numero == 0):
     print ("Tu número es cero")

else:
     print ("NEGATIVO")     """      


""" #Par o Impar 
numero = int (input("Ingresa un número: "))

if (numero % 2 == 0):
     print ("PAR")

else:
     print ("Impar")      """


""" #Persna es mayor de edad 
Edad = int (input("Ingresa tu edad: "))

if (Edad >= 18):
     print ("MAYOR DE EDAD")

elif (Edad < 18):
     print ("MENOR DE EDAD")

else:
     print ("Edad")  
 """



""" #Mayor de dos números 
numero_1 = int(input("Ingresa el primer número: "))     
numero_2 = int(input("Ingresa el segundo número: "))

if (numero _1 > numero_2):
    print("Es mayor es: ", numero_1)

elif (numero_2 > numero_1):
    print("El mayor es", numero_2)

else: 
    print("Los numeros son iguales")       """  


""" #Clasificar una calificación 
#la calificación debe estar entre 0 y 10
#Si es mayor o igula a 9 -> "Excelente"
#Si es mayor o igaul a 8 -> "Muy bien"
#Si es mayor o igaul a 6 -> "Aprobado"
#Si es menor a 6 -> "Reprobado" """

""" calificación = float (input("Ingresa la calificaión "))

if (calificación < 0 or calificación > 10 ):
    print("CALIFICACIÓN INVÁLIDA")

elif ((calificación >=9 )):
    print("Excelente")    

elif ((calificación >=8 )):
    print("Muy bien")     

elif ((calificación >=6 )):
    print("Aprobado")    

else:
    print("Reprobado")   """   """
 """


""" # Descuento de una compra
# Si el monto total es mayor o igual a $1000
# aplicar descuento del 10%
# Si es menor de $1000 hacer cobro normal
total_compra = float (input("Ingresa el total: "))

if(total_compra >=1000):
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print("El total final es: ", total_final)

else:
    print("El total es: ", total_compra)    """ 


""" #Acceso con 2 requisitos
#Solicitar edad e identificación
#and -> ("Y") Ambas condiciones se cumplen
#or -> ("O") Solo una condición se cumple
edad = int(input("Ingresa tu edad: "))
identificacion = input("¿Tienes identificación: ")

#SI, si, Si, si
#Trasformar a minusculas
respuesta = identificacion.lower()
 """



usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == "admin":
    print("Usuario correcto")
    if (contrasena == "admin123"):
        print("Bienvenido")

    else:
        print("Contrasena incorrecta")

else: 
    print("Usuario incorrecto")
    