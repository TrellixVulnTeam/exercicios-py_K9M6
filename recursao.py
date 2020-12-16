"""
n! = n*(n-1) * n(n-2)*...*1
f(n) = n*(n-1), se n>1
"""

def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero -1)

def fatorial_for(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

print(fatorial_for(5))