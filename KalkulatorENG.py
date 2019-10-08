#Calculator

print("---CALCULATOR---")

def menu():
    print("1-adding")
    print("2-substraction")
    print("3-multiplication")
    print("4-division")
    print("5-author")
    print("6-end")
    return

def dodawanie():
    a = input("First number: ")
    b = input("Second number: ")
    wynik = float(a) + float(b)
    return wynik

def odejmowanie():
    a = input("First number: ")
    b = input("Second number: ")
    wynik = float(a) - float(b)
    return wynik

def mnożenie():
    a = input("First number: ")
    b = input("Second number:")
    wynik = float(a)*float(b)
    return wynik

def dzielenie():
    a = input("First number: ")
    b = input("Second number: ")
    wynik = float(a)/float(b)
    return wynik

def autor():
    wynik = "Author: MaTeusz"
    return wynik


print(menu())
operacja = input("Co wybierasz? ")
while operacja != "9":
    if operacja == "1":
        print("\nYou have chosen add option", dodawanie())
    elif operacja == "2":
        print("\nYou have chosen subtract option", odejmowanie())
    elif operacja == "3":
        print("\nYou have chosen multiplication option", mnożenie())
    elif operacja == "4":
        print("\nYou have chosen division option", dzielenie())
    elif operacja == "5":
        print("\nYou have chosen author option", autor())
    elif operacja == "6":
        break
    else:
        print("Error menu")
    operacja = input("What you choose? ")
    