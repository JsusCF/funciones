def superficie_rectangulo(l1, l2):
    rectangulo = l1 * l2
    return rectangulo


print("Primer rectangulo")
lado1 = int(input("Ingrese el largo del rectangulo: "))
lado2 = int(input("Ingrese el ancho del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectangulo(lado1, lado2))
print("segundo rectangulo")
lado3 = int(input("Ingrese el largo del rectangulo: "))
lado4 = int(input("Ingrese el ancho del rectangulo: "))
print("La superficie del rectangulo es", superficie_rectangulo(lado3, lado4))
if superficie_rectangulo(lado1, lado2) > superficie_rectangulo(lado3, lado4):
    print("El primer rectangulo tiene una mayor superficie")
else:
    print("El segundo rectangulo tiene una mayor superficie")