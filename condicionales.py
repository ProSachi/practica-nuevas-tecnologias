edad_cliente = int(input("Deme su edad: "))
mi_lista = [2]

if mi_lista:
    print("Si tiene elementos")
else:
    print("No tiene elementos")

if edad_cliente >= 18 and edad_cliente < 60:
    # Este bloque solo se ejecuta si la condición es Verdadera (True)
    print("Cliente apto para crédito.")
if edad_cliente >= 16 or edad_cliente > 10:
    # Se evalúa solo si el 'if' anterior fue Falso
    print("Cliente requiere codeudor.")
else:
    # Se ejecuta si todas las condiciones anteriores fueron Falsas
    print("Cliente rechazado por edad.")
