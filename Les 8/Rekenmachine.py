import sys


def menu():
    """Geeft het welkom- en keuzemenu weer"""
    return("Welkom bij de rekenmachine! \n"
          "Kies een bewerking:\n"
          "1. Optellen (+)\n"
          "2. Aftrekken (-)\n"
          "3. Vermenigvuldigen (*)\n"
          "4. Delen (/)\n")


def user_input():
    """Vraagt de bewerking en twee getallen op en geeft (bewerking, getal_1, getal_2) terug."""
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
    """Geeft de output door de getallen door middel van de gemaakte keuze"""
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
    """Geeft het symbool dat hoort bij de gekozen bewerking (1-4)."""
    symbolen = {
        1: "+",
        2: "-",
        3: "*",
        4: "/"
    }
    return symbolen.get(bewerking)

def input_herhaling():
    """Vraagt of de gebruiker wil herhalen en geeft True/False terug."""
    antwoord = input("\nWil je nog een berekening doen? (ja/nee): ")
    return antwoord == "ja"



def main():

    while True:
        print(menu())
        resultaat = user_input()

        bewerking, getal_1, getal_2 = resultaat
        uitkomst = output(getal_1, bewerking, getal_2)

        symbool = get_symbool(bewerking)

        print(f"\nResultaat: {getal_1} {symbool} {getal_2} = {uitkomst}")

        if not input_herhaling():
            print("Tot ziens!")
            break


print(main())



