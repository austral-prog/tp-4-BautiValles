def leap_year():
    año = float(input("Ingrese un año: "))
    Div4 = año / 4
    Div100 = año / 100
    Div400 = año / 400
    if ((Div4 - int(Div4) ) == 0.0):
        if ((Div100 - int(Div100) ) == 0.0):
            if ((Div400 - int(Div400) ) == 0.0):
                print(f"El año {int(año)} es bisiesto")
            else:
                print(f"El año {int(año)} no es bisiesto")
        else:
            print(f"El año {int(año)} es bisiesto")
    else:
        print(f"El año {int(año)} no es bisiesto")
