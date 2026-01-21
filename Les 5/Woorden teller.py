# Woorden tellen:
# programmeer een applicatie die telt hoeveel woorden er in een zin staan.
# bonus: maak het mogelijk om een zin in te geven en het aantal woorden te tellen.
#
zin = input("Geef een zin waarvan je het aantal woorden wilt: ")
aantal_woorden = 1

for word in zin:
    if word == " ":
        aantal_woorden +=1
    else:
        aantal_woorden +=0

print(aantal_woorden)


# zin = "dit is een testzin om te testen of dit programma werkt"
# aantal_woorden = {}
#
# woorden = zin.split()
# for woord in woorden:
#     if woord in aantal_woorden:
#         aantal_woorden[woord] += 1
#     else:
#         aantal_woorden[woord] = 1
#
# print(aantal_woorden)