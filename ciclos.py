# while condicion: 
# Bloque de código a ejecutar mientras la condición sea True

# contador = 0
# while contador < 100:
#     contador += 1
#     if contador % 3 == 0 :
#         continue
#     else:
#         print("Contador:", contador)
    
# secuencia = []
# for elemento in secuencia: 
# Bloque de código a ejecutar para cada elemento

# for i in range(5):
#     print("Iteración:", i)


# Genera números del 1 al 5 print(i)

# for p in "python":
#     print(p)


def arroz_con_huevo(numero_limite):
    arroz = int(input("Indique el numero que quiere reemplazar por el arroz: "))
    huevo = int(input("Indique el numero que quiere reemplazar por el huevo: "))
    contador = 0
    while contador < numero_limite:
        contador += 1
        if contador % arroz == 0 and contador % huevo==0:
            print("Arroz Con Huevo")
            continue
        elif contador % arroz == 0:
            print("Arroz")
        elif contador % huevo == 0:
            print("Huevo")
        else:
            print(contador)

numero_limite = int(input("Hasta que numero deseas realizar la validación: "))

arroz_con_huevo(numero_limite)