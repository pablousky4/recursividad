def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Ejemplo de uso
numero = 10
print(f"El {numero}-ésimo número de Fibonacci es: {fibonacci_recursivo(numero)}")