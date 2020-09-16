#Quispe Gutierrez Alan Herlan
#C.I.:9919482
#Utilizando los coeficientes (a,b,c) de una ecuacion de segundo grado se pide mostrar 
# la naturaleza de sus raices
print("sabiendo que Ax^2-Bx-C dijite los numeros")
a=int(input("--A-- Ingrese un numero:\n "))
b=int(input("--B-- Ingrese un numero:\n "))
c=int(input("--C-- Ingrese un numero:\n "))
R=(b**2)-4*(a*c)
if (R>0):
    print("El discriminante",R,"son reales y diferentes")
elif (R==0):
    print("El descriminante",R,"son reales e iguales")
elif (R<0):
    print("El discriminante",R,"son complejas")