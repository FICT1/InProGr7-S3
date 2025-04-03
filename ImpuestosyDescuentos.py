#Ejercicio 7: Cálculo del precio final de un producto con impuestos y descuentos

#1. Ingresar el precio original del producto.
#2. Ingresar el porcentaje de descuento aplicado.
#3. Multiplicar el precio por el porcentaje de descuento.
#4. Dividir el resultado entre 100.
#5. Restar el descuento del precio original.
#6. Guardar el resultado como precio con descuento.
#7. Ingresar el porcentaje de IVA.
#8. Multiplicar el precio con descuento por el IVA.
#9. Dividir el resultado entre 100.
#10. Sumar el impuesto al precio con descuento.
#11. Guardar el resultado como precio final.
#12. Mostrar el precio original, el descuento aplicado, el precio con descuento, el IVA calculado y el precio final. 
precio_neto=float(input("Ingresar el precio original del producto: "))
porcentaje_descuento=float(input("Ingresar el porcentaje del descuento aplicado: "))
descuento=(precio_neto*porcentaje_descuento)/100
precio_descuento=precio_neto-descuento
IVA=15
impuesto=(precio_descuento*IVA)/100
precio_final=impuesto+precio_descuento
print ("*********************************************************************")
print ("El precio original es: ", precio_neto )
print ("EL descuento aplicado es: ", descuento )
print ("El precio con descuento es: ", precio_descuento )
print ("El IVA calculado es: ", IVA)
print ("El precio final es: ", precio_final )
print ("*********************************************************************")
