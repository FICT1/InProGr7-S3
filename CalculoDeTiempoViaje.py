#ejercicio 4
duracionprimertramo=float(input("Ingresar la duracion del primer vuelo " ))
duracionprimeraescala=float(input("Ingresar la duracion de la primera escala " ))
duracionsegundotramo=float(input("Ingresar la duracion del segundo tramo del vuelo " ))
duracionsegundaescala=float(input("Ingresar la duracion de la segunda escala " ))
duraciontercertramo=float(input("Ingresar la duracion del tercer tramo "))
#6. Sumar la duración del primer tramo con la primera escala.
#7. Sumar el resultado con el segundo tramo del vuelo.
#8. Sumar el resultado con la segunda escala.
#9. Sumar el resultado con el tercer tramo del vuelo.
#10. Mostrar el tiempo total del viaje. 
tiempototalviaje1=duracionprimertramo+duracionprimeraescala
tiempototalviaje2=tiempototalviaje1+duracionsegundotramo
tiempototalviaje3=tiempototalviaje2+duracionsegundaescala
tiempototalviaje4=tiempototalviaje3+duraciontercertramo
print ("El tiempo total de tu viaje es de: ", tiempototalviaje4)
