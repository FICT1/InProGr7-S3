#Ejercicio 9: Cálculo del tiempo total de una película con comerciales

#1. Ingresar la duración de la película en minutos.
#2. Ingresar la duración de los comerciales previos.
#3. Ingresar la cantidad de pausas comerciales durante la película.
#4. Ingresar la duración de cada pausa comercial.
#5. Multiplicar la cantidad de pausas por la duración de cada pausa.
#6. Guardar el resultado como total de comerciales durante la película. 
#7. Sumar la duración de la película con los comerciales previos.
#8. Sumar el resultado con los comerciales durante la película.
#9. Guardar el resultado como duración total.
#10. Mostrar la duración original de la película.
#11. Mostrar la duración de los comerciales totales.
#12. Mostrar el tiempo total de la proyección. 
duracion_pelicula = int(input("Ingrese la duración de la película en minutos: "))
comerciales_previos = int(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales: "))
duracion_pausa = int(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales_durante = cantidad_pausas * duracion_pausa
subtotal = duracion_pelicula + comerciales_previos
duracion_total = subtotal + total_comerciales_durante

print("**************************************************************************************************")
print("Duración original de la película:", duracion_pelicula, "minutos")
print("Duración total de los comerciales:", total_comerciales_durante + comerciales_previos, "minutos")
print("Tiempo total de la proyección:", duracion_total, "minutos")
print("**************************************************************************************************")
