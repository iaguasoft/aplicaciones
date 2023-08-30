# Definir los valores de entrada
monto_pesos_mexicanos = float(input("Ingresa el monto en pesos mexicanos: "))
tipo_cambio_pesos_a_dolares = float(input("Ingresa el tipo de cambio de pesos mexicanos a dólares: "))
tipo_cambio_dolares_a_pesos_argentinos = float(input("Ingresa el tipo de cambio de dólares a pesos argentinos: "))

# Calcular la conversión de pesos mexicanos a dólares
monto_dolares = monto_pesos_mexicanos / tipo_cambio_pesos_a_dolares

# Calcular la conversión de dólares a pesos argentinos
monto_pesos_argentinos = monto_dolares * tipo_cambio_dolares_a_pesos_argentinos

# Mostrar los resultados
print(f"El monto en dólares es: {monto_dolares}")
print(f"El monto en pesos argentinos es: {monto_pesos_argentinos}")

