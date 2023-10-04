#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

#No hay declaración de variables
#una variable se crea con la primera asignación
numero = 5
texto = "hola"

print(numero)
print(texto)

numero = "cinco" #No se produce error al asignar valores de otro tipo diferente al inicial
#Esto se carga la variable y crea otra con el tipo de dato adecuado

print(numero)

numero = str(5) #Convierte el 5 en un string

#devuelve el tipo de la variable
print(type(numero))

numero = 5

print(type(numero))

texto = "Aaaaa'a'aaa"
print(texto)

#Variables case sensitive
a = "variable a"
A = "variable b"

print(a+" "+A)

#Asignacion de valores abreviada. Si se ponen de más se asignan los extra a la última variable. Si son menos se quedán variables sin valores
x, y, z = "Orange", "Banana", "Cherry"
print(x+" "+y+" "+z)

#Asignacion del mismo valor a varias variables
x = y = z = "Orange"
print(x+" "+y+" "+z)

#Unpacking de arrays
fruits = ["apple","banana","cherry"]
x, y ,z =fruits
print(x+" "+y+" "+z)

#print de variables con comas
print(x,y,z)#Imprime con espacio entre variables