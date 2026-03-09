MONTOIRP = 80000000
sueldoMensual = 5000000  # sueldo mensual fijo

# Calcular el sueldo anual
sueldoAnual = sueldoMensual * 12

# Verificar si supera el monto establecido
if sueldoAnual > MONTOIRP:
    print("Esta persona debe pagar impuestos")
else:
    print("La persona NO debe abonar impuestos")
