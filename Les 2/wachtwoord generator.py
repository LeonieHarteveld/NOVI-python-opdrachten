# Schrijf een programma dat een gebruiker om een wachtwoord vraagt. De gebruiker heeft maximaal 3 pogingen om het juiste wachtwoord in te voeren. Als het juiste wachtwoord is ingevoerd, print je een succesbericht en beëindig je de loop. Als de gebruiker 3 pogingen fout invoert, geef je een bericht dat de toegang is geweigerd.
#
# Stappenplan:
#
# 1. Stel een vast wachtwoord in (bijvoorbeeld: "python123"), door daar een variabele voor te maken.
# 2. Vraag de gebruiker om het wachtwoord in te voeren.
# 3. Gebruik een while-loop om de gebruiker maximaal 3 kansen te geven om het juiste wachtwoord in te voeren.
# 4. Als de gebruiker het juiste wachtwoord invoert, beëindig dan de loop met een succesbericht.
# 5. Als de gebruiker na 3 pogingen nog steeds het verkeerde wachtwoord invoert, geef een foutmelding.

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Je bent ingelogd")
    else:
        attempts += 1
        print(f"Password incorrect. Poging {attempts}/{max_attempts}")

if attempts == max_attempts:
    print("Password te vaak fout")

