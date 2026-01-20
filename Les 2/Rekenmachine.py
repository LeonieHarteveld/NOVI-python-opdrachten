# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.

# Voorbeeld:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.

print("Reken je som uit:")
num1 = float(input("Voer een getal in: "))
num2 = float(input("Voer je tweede getal in: "))
operatie = input("Wil je delen (/), vermenigvuldigen (*), aftrekken (-) of optellen (+)? ")

if operatie == "/":
    print(f"Je uitkomst is {num1 / num2}")
elif operatie == "*":
    print(f"Je uitkomst is {num1 * num2}")
elif operatie == "+":
    print(f"Je uitkomst is {num1 + num2}")
elif operatie == "-":
    print(f"Je uitkomst is {num1 - num2}")
else:
    print("Invoer is ongeldig")


