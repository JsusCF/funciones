def cantidad_de_a(palabra):
    cant = 0
    for i in range(len(palabra)):
        if (palabra[i] == "a") or (palabra[i] == "A"):
            cant += 1
    return cant


palab = input("Ingrese una palabra: ")
print("La palabra", palab, "tiene", cantidad_de_a(palab), "letras a")