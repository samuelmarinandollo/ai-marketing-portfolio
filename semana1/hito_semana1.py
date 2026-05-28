def main():
    nombre = input("Como te llamas ")
    edad = input("Cuantos años tienes ")
    presentar(nombre, edad)


def presentar(nombre, edad):
    print(f"Hola, soy {nombre} y tengo {edad} años")


main()
