#ejemplo 3

salariobrut=float(input("Ingresar el salario bruto del empleado"))
impues=salariobrut*0.1
segurosoc=salariobrut*0.05
fondopen=salariobrut*0.03
descuentototal=(impues+segurosoc+fondopen)
salarionet=salariobrut-descuentototal
print ("*************************************************************")
print ("El salario Bruto final es: ", salariobrut )
print ("Los descuentos totales son: ", descuentototal)
print ("El salario neto es: ", salarionet)
print ("*************************************************************")



