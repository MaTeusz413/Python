#kalkulator

print("---KALKULATOR---")

def menu():
    print("1-dodawanie")
    print("2-odejmowanie")
    print("3-mnożenie")
    print("4-dzielenie")
    print("5-autor")
    print("6-koniec")
    return

def dodawanie():
    a = input("Pierwsza liczba: ")
    b = input("Druga liczba ")
    wynik = float(a) + float(b)
    return wynik

def odejmowanie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) - float(b)
    return wynik

def mnożenie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a)*float(b)
    return wynik

def dzielenie():
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a)/float(b)
    return wynik

def autor():
    wynik = "Autor: MaTeusz"
    return wynik


print(menu())
operacja = input("Co wybierasz? ")
while operacja != "9":
    if operacja == "1":
        print("\nWybrałeś opcję dodawania", dodawanie())
    elif operacja == "2":
        print("\nWybrałeś opcję odejmowania", odejmowanie())
    elif operacja == "3":
        print("\nWybrałeś opcję mnożenia", mnożenie())
    elif operacja == "4":
        print("\nWybrałeś opcję dzielenia", dzielenie())
    elif operacja == "5":
        print("\nWybrałeś opcję informacji o autorze", autor())
    elif operacja == "6":
        break
    else:
        print("Błędne menu")
    operacja = input("Co wybierasz? ")
    