#Ejercicio 8: Conversión de una cantidad en dólares a distintas monedas

#1. Ingresar la cantidad en dólares.
#2. Definir la tasa de cambio de dólares a euros.
#3. Definir la tasa de cambio de dólares a libras.
#4. Definir la tasa de cambio de dólares a yenes.
#5. Multiplicar la cantidad en dólares por la tasa de cambio a euros.
#6. Guardar el resultado como cantidad en euros.
#7. Multiplicar la cantidad en dólares por la tasa de cambio a libras.
#8. Guardar el resultado como cantidad en libras.
#9. Multiplicar la cantidad en dólares por la tasa de cambio a yenes.
#10. Guardar el resultado como cantidad en yenes.
#11. Mostrar la cantidad en dólares.
#12. Mostrar la cantidad convertida en euros, libras y yenes. 
dolares = int(input("Ingresar la cantidad de billetes en dolares: "))
euros = 0.96 * dolares
libras = 0.77 * dolares
yenes = 147.47 * dolares
print("********************************************************")
print("Tus", dolares, "dolares en euros son:", euros, "euros")
print("Tus", dolares, "dolares en libras son:", libras, "libras")
print("Tus", dolares, "dolares en yenes son:", yenes, "yenes")
print("********************************************************")