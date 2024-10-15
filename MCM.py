import math

# Función para calcular el MCM de dos números
def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Función para calcular el MCM de más de dos números
def mcm_de_varios_numeros(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado = mcm(resultado, numeros[i])
    return resultado

# Ejemplo de uso
numeros = [4, 5, 6, 8]
resultado = mcm_de_varios_numeros(numeros)
print(f"El MCM de {numeros} es: {resultado}")
