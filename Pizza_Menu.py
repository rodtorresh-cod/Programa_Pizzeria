def menu_tamaños():
    print("====== MENU PIZZA ======")
    print("1. Pequeña - $99")
    print("2. Mediana - $149")
    print("3. Grande - $229")

def menu_bebidas():
    print("===== MENU BEBIDAS =====")
    print("1. Coca Cola - $35")
    print("2. Pepsi - $25")
    print("3. Fanta - $15")


def elegir_tamaño():
    tamaño = 0
    precio = 0
    nombre = ""
    if tamaño not in [1,2,3]:
        menu_tamaños()
        tamaño = int(input("Elije tamaño(1-3): "))

        if tamaño == 1:
            precio = 99
            nombre = "Pequeña"
        elif tamaño == 2:
            precio = 149
            nombre = "Mediana"
        elif tamaño == 3:
            precio = 229
            nombre = "Grande"
        else:
            print("Error: Debes elegir un tamaño primero")

    return nombre, precio

def elegir_bebida():
    bebida = 0
    precio = 0
    nombre = ""
    if bebida not in [1, 2, 3]:
        menu_bebidas()
        bebida = int(input("Elije Bebida(1-3): "))

        if bebida == 1:
            precio = 35
            nombre = "Coca Cola"
        elif bebida == 2:
            precio = 25
            nombre = "Pepsi"
        elif bebida == 3:
            precio = 15
            nombre = "Fanta"
        else:
            print("Error: Debes elegir una bebida primero")

    return nombre, precio    

def main():
    nombre, total = elegir_tamaño()
    nombre, total = elegir_bebida()

    print("-------------------------------")
    print("       TOTAL DE LA COMPRA    ")
    print("-------------------------------")
    print(f"Tamaño: {nombre}")
    print("Total a pagar: $", total)
    print("-------------------------------")
    print("¡Gracias por tu compra!")

main()