def calcular_impuesto(precio_base, porcentaje_impuesto):
    # Lógica encapsulada
    impuesto = precio_base * (porcentaje_impuesto / 100)
    precio_final = precio_base + impuesto
    return precio_final # Devuelve el valor calculado

# Uso de la función
total = calcular_impuesto(100, 19)

def calcular_impuesto2(precio_base, porcentaje_impuesto):
    # Lógica encapsulada
    impuesto = precio_base * (porcentaje_impuesto / 100)
    precio_final = precio_base + impuesto
    print("El precio final es: ", precio_final)

# Uso de la función
calcular_impuesto2(100, 19)
