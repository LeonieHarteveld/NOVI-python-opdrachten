import sys


def menu():
    return("Welkom bij de rekenmachine! \n"
          "Kies een bewerking:\n"
          "1. Optellen (+)\n"
          "2. Aftrekken (-)\n"
          "3. Vermenigvuldigen (*)\n"
          "4. Delen (/)\n")

def user_input():
    try:
        bewerking = int(input("Voer de nummer van de bewerking in (1/2/3/4): "))
        getal_1 = int(input("Voer het eerste getal in: "))
        getal_2 = int(input("Voer het tweede getal in: "))
        return bewerking, getal_1, getal_2

    except ValueError:
        print("U heeft geen geheel getal in gevoerd", file=sys.stderr)

    except TypeError:
        print("U heeft geen getal ingevoerd ", file=sys.stderr)

def output(getal, bewerking, getal2):
    try:
        if bewerking == 1:
            return getal + getal2
        elif bewerking == 2:
            return getal - getal2
        elif bewerking == 3:
            return getal * getal2
        elif bewerking == 4:
            return getal / getal2
    except ZeroDivisionError:
        print("U mag niet delen door 0 ", file=sys.stderr)


def get_symbool(bewerking):
    symbolen = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }
    return symbolen.get(bewerking)

def input_herhaling():
    herhalen = input("Wil je nog een berekening doen? (ja/nee): ")


def main():
    print(menu())

    resultaat = user_input()

    bewerking, getal_1, getal_2 = resultaat
    uitkomst = output(getal_1, bewerking, getal_2)

    symbool = get_symbool(bewerking)

    return f"\nResultaat: {getal_1} {symbool} {getal_2} = {uitkomst}"


print(main())



