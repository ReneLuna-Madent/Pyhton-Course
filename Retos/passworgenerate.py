import random


def generar_contrasena():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbol = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayus + minus + symbol + numbers

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()
