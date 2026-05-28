color = input( "Dime un color " )
match color :
    case "rojo":
        print ("Parar")
    case "verde":
        print("seguir")
    case "amarillo":
        print("precaucion")
    case _ :
        print ("color no valido, dime otro")
