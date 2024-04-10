def calcular_operacion(primer_factor, segundo_factor, sumando):
    operacion = primer_factor * segundo_factor + sumando
    return operacion

def registrar_numeros():
    primer_numero = 5
    segundo_factor = 3
    tercer_factor = 7
    resultado = calcular_operacion(primer_numero, segundo_factor, tercer_factor)
    print("El resultado es:", resultado)

registrar_numeros()