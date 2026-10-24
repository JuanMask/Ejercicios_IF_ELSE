#estructura if else
#es una estructura condicional qye permite que un 
#programa elija que instrucciones ejecutar
#dependiendo si una condicion se cumple o no

#una condicion es una expresion que python
#evalua como verdadera (true) o falsa (false)

#operadpores de comparacion 
""" ==igual a 
!= distinto de 
> mayor que 
< menor que
>= mayor o igual que 
<= menor o igual que   """

# if else y elif

""" if condicion:
    instrucciones_si_verdadero

elif(condicion_2):
    instrucciones_si_verdadero_2
    
else:
    instrucciones_si_falso """

#ejemplos
#positibvo,negativo o cero
""" numero = int(input("ingredsa un numero: "))

#condicional
if (numero >0):
    print("positivo")
elif (numero == 0):
    print("tu numero es cero: ")
else:
    print("negativo") """

#par o impar 

""" numero = int(input("ingresa un numero: "))

if (numero % 2 == 0):
    print("par")
else:
    print("impar")
     """

#persona es mayo de edad
""" edad = int(input("ingresa tu edad: "))
if (edad >= 18):
    print("eres mayor de edad")
else:
    print("eres menor de edad")
 """

#mayor de dos numeros
""" numero_1 = int(input("ingresa el primer numero: "))
numero_2 = int(input("ingresa el segundo numero"))

if (numero_1 > numero_2):
    print("es mayor el ", numero_1)

elif (numero_2 > numero_1):
    print("el mayor es: ",numero_2)

else:
    print("los numeros son iguales") """

#clasificar una calificacion 
#la calificacion debe estar entre 0 y 10

#si es mayor o igual a 9 ->"excelente"
#si es mayor o igual a 8 ->"muy bien"
#si es mayor o igual a 6 ->"aprobado"
#si es menor o igual a 6 ->"reprobado"

""" calificacion = float(input("ingresa tu calificacion: "))
if calificacion < 0 or calificacion >10:
    print("calificacion invalida")
elif(calificacion >= 9):
    print("excelente")
elif(calificacion >= 8):
    print("muy bien")
elif(calificacion >= 6):
    print("aprobado")
else:
    print("reprobado") """

#descuento de una compra
#si el monto total es mayor a 1000 aplicar descuento del 10%
#si es menor de 1000 hacer cobro normal

""" total_compra = float(input("ingresa el total : "))
if (total_compra >= 1000):
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print("el total final es : ", total_final)

else:
    print("el total es: ",total_compra) """

#acceso con dos requisitos
#solicitar edad e identificacion 
#and -> ("Y") ambas condiciones se sumplen
#or ->("O") solo una condicion se cunmple
""" edad = int(input("ingresa tu edad: "))
identificacion = input("tienes identificacion: ")

#SI, si, Si, sI
#TRANSFORMA A MINUSCULAS 
respuesta = identificacion.lower()
if edad >= 18 and respuesta =="si":
    print("acceso permitido")
else:
    print("acceso denegado")
 """

#condicion anidada
#usuario: admin
#contraseña : admin123
usuario = input("usuario: ")
contrasena = input("contraseña: ")
if usuario == "admin":
    if (contrasena == "admin123"):
        print("bienvenido")
    else: 
        print("contraseña incorrecta")
   
else:
    print("usuario incorrecto")




























