menu = """
    Bienvenido a Madent Coins

    1 Pesos Mexicanos
    2 Pesos Argentinos
    3 Pesos Brasileños
    4 Pesos Colombianos

    Por favor Elige la opcion de 
    tu moneda de origen de cambio:  """

opcion =int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuantos Pesos Mexicanos Tienes?: "))
    valor_madentcoins = 21.04
    madentcoins = pesos / valor_madentcoins
    madentcoins = round(madentcoins, 2)
    madentcoins = str(madentcoins)
    print("Tienes $" + madentcoins + "Madentcoins ")

elif opcion ==2:
    pesos = float(input("¿Cuantos Pesos Argentinos Tienes?: "))
    valor_madentcoins = 65
    madentcoins = pesos / valor_madentcoins
    madentcoins = round(madentcoins, 2)
    madentcoins = str(madentcoins)
    print("Tienes $" + madentcoins + "Madentcoins ")

elif opcion ==3:
    pesos = float(input("¿Cuantos Pesos Brasileños Tienes?: "))
    valor_madentcoins = 35
    madentcoins = pesos / valor_madentcoins
    madentcoins = round(madentcoins, 2)
    madentcoins = str(madentcoins)
    print("Tienes $" + madentcoins + "Madentcoins ")

elif opcion ==4:
    pesos = float(input("¿Cuantos Pesos Colombianos Tienes?: "))
    valor_madentcoins = 4200
    madentcoins = pesos / valor_madentcoins
    madentcoins = round(madentcoins, 2)
    madentcoins = str(madentcoins)
    print("Tienes $" + madentcoins + "Madentcoins ")

else:
    print("ingresa una opcion correcta please :)")
