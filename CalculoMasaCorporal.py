#Ejercicio 6: Cálculo del índice de masa corporal (IMC)

#1. Ingresar el peso en kilogramos.
#2. Ingresar la altura en metros.
#3. Multiplicar la altura por sí misma.
#4. Dividir el peso entre el resultado anterior.
#5. Guardar el resultado como IMC.
#6. Multiplicar el IMC por 100.
#7. Dividir el resultado entre 100 para redondearlo a dos decimales.
#8. Mostrar el peso ingresado.
#9. Mostrar la altura ingresada.
#10. Mostrar el valor del IMC calculado.
#11. Mostrar la clasificación del IMC según los valores estándar
kilos=float(input("Ingresar el peso en kilogramos: "))
altura=float(input("Ingresar la altura en metros: "))
IMC=kilos/(altura*altura)
IMC=round(IMC, 2)
print ("***************************************")
print ("El peso es: ",kilos )
print ("Tu altura es: ", altura)
print ("El valor de tu IMC es: ", IMC)
if IMC < 18.5:
    print("Clasificación: Bajo peso")
elif IMC >= 18.5 and IMC < 25:
    print("Clasificación: Peso normal")
elif IMC >= 25 and IMC < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
print ("***************************************")


