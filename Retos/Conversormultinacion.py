def conversor(tipo_pesos, valor_madentcoins):
    pesos = float(input("¿Cuantos Pesos" + tipo_pesos + "Tienes?: "))
    madentcoins = pesos / valor_madentcoins
    madentcoins = round(madentcoins, 2)
    madentcoins = str(madentcoins)
    print("Tienes $" + madentcoins + "Madentcoins ")


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
   conversor("Mexicanos", 21.04)
elif opcion ==2:
    conversor("Argentinos", 4200)
elif opcion ==3:
    conversor("Brasileños", 65)
elif opcion ==4:
    conversor("Colombianos", 3875)

else:
    print("ingresa una opcion correcta please :)")
