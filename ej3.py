age = int(input("Cuantos años tienes "))
carnet = input("Tienes carnet? si/no ")
if age >= 18 and carnet == "si":
    print("Puede conducir")
else:
    print("No puede conducir")