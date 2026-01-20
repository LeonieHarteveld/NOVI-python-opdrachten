# Tafels

# Schrijf een programma dat de tafel van een getal afdrukt.
# De gebruiker voert een getal in en het programma drukt de tafel van dat getal af.
# De tafel van 7 ziet er bijvoorbeeld als volgt uit:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Probeer het eerst zonder loop,

getal_invoer = int(input("Voer hier uw getal in: "))
print(f"{getal_invoer} x 1 = {getal_invoer * 1}")
print(f"{getal_invoer} x 2 = {getal_invoer * 2}")
print(f"{getal_invoer} x 3 = {getal_invoer * 3}")
print(f"{getal_invoer} x 4 = {getal_invoer * 4}")
print(f"{getal_invoer} x 5 = {getal_invoer * 5}")
print(f"{getal_invoer} x 6 = {getal_invoer * 6}")
print(f"{getal_invoer} x 7 = {getal_invoer * 7}")
print(f"{getal_invoer} x 8 = {getal_invoer * 8}")
print(f"{getal_invoer} x 9 = {getal_invoer * 9}")
print(f"{getal_invoer} x 10 = {getal_invoer * 10}")

# Probeer het nu met een loop.

getal_invoer2 = int(input("Voer een getal in: "))

for getal in range(1,11):
    print(f"{getal_invoer2} * {getal} = {getal_invoer2 * getal}")

# --------------------------------------------------------------------------------------------

# Optellen
# Schrijf een programma dat de som van alle getallen tot een bepaalde limiet berekent.

# Bijvoorbeeld: de som van alle getallen tot 3 is 6 (1 + 2 + 3 = 6)

invoer = int(input("Voer een getal in: "))
teller = 1
som = 0

while som <= invoer:
    som += teller
    teller += 1
print(f"De som van de getallen {invoer} is {som}")

# --------------------------------------------------------------------------------------------

# Dit is een klassieke programmeeroefening die vaak wordt gebruikt in sollicitatiegesprekken.
# FizzBuzz

# Schrijf een programma dat de getallen van 1 tot 100 afdrukt.

for getal in range(1, 101):
    if getal % 3 == 0 and getal % 5 == 0:
        print("FizzBuzz")
    elif getal % 3 == 0:
        print("Fizz")
    elif getal % 5 == 0:
        print("Buzz")
    else:
        print(getal)

# Maar voor veelvouden van drie, druk "Fizz" af in plaats van het getal.


# En voor veelvouden van vijf, druk "Buzz" af.
# Voor veelvouden van zowel drie als vijf, druk "FizzBuzz" af.


