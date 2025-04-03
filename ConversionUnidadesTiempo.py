#Ejercicio 5: Conversión de unidades de tiempo

#1. Ingresar la cantidad total de segundos.
#2. Dividir los segundos entre 3600 para obtener las horas.
#3. Guardar la parte entera del resultado como horas.
#4. Multiplicar las horas obtenidas por 3600.
#5. Restar ese valor de la cantidad total de segundos.
#6. Dividir el resultado entre 60 para obtener los minutos.
#7. Guardar la parte entera del resultado como minutos.
#8. Multiplicar los minutos obtenidos por 60.
#9. Restar ese valor del resultado anterior para obtener los segundos restantes.
#10. Mostrar las horas, minutos y segundos. 
segundos=int(input("Ingresar cantidad total de segundos: "))
horas=3600/segundos
h1=horas*3600
h2=h1-segundos
minutos=h2/60
h3=minutos*60
segundosrestantes=h3-60
print("Horas: ", horas)
print("Minutos: ", minutos)
print("Segundos: ", segundos)

