def sumar_digitos(numero):
    # Caso base
    if numero < 10:
        return numero
    else:
        # Caso recursivo
        return numero % 10 + sumar_digitos(numero // 10)

# Ejemplo
numero = 2468
resultado = sumar_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")
