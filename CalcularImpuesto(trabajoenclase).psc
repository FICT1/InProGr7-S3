Algoritmo CalcularImpuesto
	definir precio, porc_impuesto, valor_imp, total_pago como Real
	Escribir "Dime el precio del producto"
	Leer precio
	Escribir "Dime el porcentaje de impuesto"
	Leer porc_impuesto
	porc_impuesto = porc_impuesto / 100
	escribir "Nuevo impuesto"
	valor_imp= precio*porc_impuesto
	total_pago=precio+valor_imp
	escribir "****************************************************"
	escribir precio
	escribir porc_impuesto
	escribir valor_imp
	Escribir total_pago
	escribir "****************************************************"
	
FinAlgoritmo
