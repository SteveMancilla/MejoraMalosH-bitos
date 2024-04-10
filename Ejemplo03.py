
def funcion_AreaRectangulo(altura, base):
    areaRectangulo = altura * base
    return areaRectangulo


def func_AreaTriangulo(base, altura):
    areaTriangulo = 0.5 * base * altura
    return areaTriangulo


def funcionPrincipal():
    baseRectangulo = 4
    alturaRectangulo = 6
    rectangulo_area = funcion_AreaRectangulo(baseRectangulo, alturaRectangulo)
    print("Área del rectángulo: -> ", rectangulo_area, "\n")

    baseTriangulo = 5
    alturaTriangulo = 8
    trianguloArea = func_AreaTriangulo(baseTriangulo, alturaTriangulo)
    print("Área del triángulo: -> ", trianguloArea, "\n\n")

if __name__=='__main__':
    print("\n\t\t Hallando areas del rectangulo y triangulo ")
    print("\t\t ----------------------------------------- \n\n")
    
    funcionPrincipal()