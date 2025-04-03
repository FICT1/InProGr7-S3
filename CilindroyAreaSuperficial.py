#Ejercicio 10: Cálculo del volumen de un cilindro y su área superficial

#1. Ingresar el radio del cilindro.
#2. Ingresar la altura del cilindro.
#3. Calcular el área de la base multiplicando PI por el radio al cuadrado.
#4. Multiplicar el área de la base por la altura.
#5. Guardar el resultado como volumen del cilindro.
#6. Calcular el área lateral multiplicando 2 por PI por el radio por la altura.
#7. Calcular el área total sumando el área lateral más dos veces el área de la base.
#8. Guardar el resultado como área superficial del cilindro.
#9. Mostrar el radio y la altura ingresados.
#10. Mostrar el volumen calculado.
#11. Mostrar el área superficial calculada. 

radio = float(input("Ingrese el radio del cilindro en metros: "))
altura = float(input("Ingrese la altura del cilindro en metros: "))

area_base = 3.1416 * radio * radio
volumen = area_base * altura
area_lateral = 2 * 3.1416 * radio * altura
area_superficial = area_lateral + 2 * area_base
print("******************************************************************************")
print("Radio ingresado:", radio, "metros")
print("Altura ingresada:", altura, "metros")
print("Volumen del cilindro:", volumen, "metros cúbicos")
print("Área superficial del cilindro:", area_superficial, "metros cuadrados")
print("******************************************************************************")
