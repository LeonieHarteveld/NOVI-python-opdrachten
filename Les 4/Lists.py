# ==========================================
# Voorbeeld Opdracht
# Maak een lijst aan met daarin de volgende getallen: 10, 20 en 30
#
# Voer de volgende opdrachten uit:
# - Voeg het getal 40 toe aan (het einde van) de lijst
#
# Aan het einde print je de lijst 'getallen'.
# ==========================================


# list met getallen
#getallen = [10, 20, 30]

# Voeg het getal 40 toe aan (het einde van) de lijst
#getallen.append(40)
#print('list na toevoeging 40 aan het einde van de lijst: ', getallen)  # Het resultaat is: [10, 20, 30, 40]


# ==========================================
# Opdracht 1:
# Maak een lijst met daarin de volgende getallen: 2, 4, 7, 11 en 19
# Voer de volgende opdrachten uit:
# - Voeg het getal 22 toe aan (het einde van) de lijst
# - Voeg het getal 6 toe tussen 4 en 7
# - Vervang het getal 4 door het getal 5
# - Print de lijst 'getallen'
#
# Verwachte uitkomst: [2, 5, 6, 7, 11, 19, 22]
# ==========================================

getallen_opdracht_1 = [2, 4, 7, 11, 19]
getallen_opdracht_1.append(22)
getallen_opdracht_1.insert(2, 6)
getallen_opdracht_1[1] = 5

print(getallen_opdracht_1)

# ==========================================
# Opdracht 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’ die een lijst als parameter meekrijgt.
# Voer de volgende opdrachten uit:
# - Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen van de Fibonacci reeks.
# - Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# - Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# - Print de waarde van de fibonacci_reeks
#
# Verwachte uitkomst:   [1, 1, 2, 3, 5, 8, 13]
# ==========================================

fibonacci_start_reeks = [1, 1]

def fibonacci_uitbreiding(fibonaccie_reeks):
    nieuw_getal = fibonaccie_reeks[-1] + fibonaccie_reeks[-2]
    fibonaccie_reeks.append(nieuw_getal)

for aantal in range(5):
    fibonacci_uitbreiding(fibonacci_start_reeks)

print(fibonacci_start_reeks)



# ==========================================
# Opdracht 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen 1 tot en met 10. Gebruik een for loop.
#
# Verwachte uitkomst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ==========================================

getallen_opdracht_3 = []

for getal in range(1, 11):
    nieuw_getal = getal * getal
    getallen_opdracht_3.append(nieuw_getal)

print(getallen_opdracht_3)