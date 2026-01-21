#Palindrome Checker
# Een Palindrome is een woord dat hetzelfde is als je het van voor naar achter leest als andersom. Bijvoorbeeld: lepel, radar en fiets zijn palindromes. Schrijf een programma dat een lijst van woorden heeft en voor elk woord aangeeft of het een palindrome is of niet.
# Het programma moet een dictionary maken waarbij de key het woord is en de value een boolean die aangeeft of het woord een palindrome is of niet.
# De dictionary moet er als volgt uitzien:
# {
#     "radar": True,
#     "fiets": False,
#     "lepel": True,
#     "python": False
# }
from dataclasses import replace

# Test in for loop

words = ['radar', 'fiets', 'lepel', 'python']

for word in words:
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Geen palindrome")

# Met dictonary

palindrome_words = {
         "radar": True,
         "fiets": False,
         "lepel": True,
         "python": False
     }
for word, boolean in palindrome_words.items():
    print(f"\nWoord: {word}")
    print(f"Boolean: {boolean}")

#Bonus
# 2 zinnen, 1 zin is geen palindrome, de andere wel uncomment de zin die je wilt testen
zin1 = "dit is een testzin om te testen of dit programma werkt"
zin2 = "eva can i see bees in a cave"

#Tip 1: Gebruik de replace() functie om alle spaties uit de zin te halen.

def spatie_verwijderen(zin) :
   zin_zonder_spaties = zin.replace(" ", "")
   return zin_zonder_spaties == zin_zonder_spaties [::-1]

print(spatie_verwijderen(zin1))
print(spatie_verwijderen(zin2))


