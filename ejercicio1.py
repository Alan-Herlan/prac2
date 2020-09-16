#Quispe Gutierrez Alan Herlan
#C.I.:9919482
#Ingerese un tiempoX que estara representado en segundos,luego ingrese el tiempo que
# tomara en realizarse una tareaZ representado en horas,minutos y segundos.
# se pide verificar si con el tiempo X se puede finalizar la tarea Z
print('Ingrese segundos:')
r=int(input())
print('Ingrese el tiempo de la tarea:')
h=int(input('hora:'))
m=int(input('minutos:'))
s=int(input('segundo:'))
x=(r//3600 and r//60)
if(x<h and x<m and x<s):
    print('Se puede finalizar la tarea')
else:
    (x>h and x>m and x>s)
    print('No se puede realizar la tarea')