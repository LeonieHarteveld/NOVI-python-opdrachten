bibliotheek = {
    "The Silent Patient": {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    },
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
        "auteur": "Tara Westover",
        "genre": "Memoir",
        "publicatiejaar": 2018
    },
    "Circe": {
        "auteur": "Madeline Miller",
        "genre": "Fantasy",
        "publicatiejaar": 2018
    }
}

#Je gaat een bibliotheekprogramma maken. Het programma moet de volgende functionaliteiten hebben:
#1. De gebruiker moet boeken kunnen toevoegen aan de bibliotheek. Een boek heeft de volgende eigenschappen:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#2. De gebruiker moet een lijst van alle boeken in de bibliotheek kunnen opvragen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#3. De gebruiker moet een lijst van alle boeken in een bepaald genre kunnen opvragen. De gebruiker moet het genre kunnen invoeren en het programma moet alle boeken in dat genre tonen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Publicatiejaar

#4. De gebruiker moet het programma kunnen stoppen.

#Een paar tips voor het maken van dit programma:
# Als je een keuze menu maakt, kun je een while loop gebruiken die blijft loopen totdat de gebruiker kiest om te stoppen.
# Je keuze menu is eigenlijk een if-elif-else statement. Je kunt de keuze van de gebruiker opslaan in een variabele en dan met if-elif-else bepalen wat er moet gebeuren.

keuze = " "

while keuze != 4 :
    print("Welkom bij de bibliotheek!\n",
      ("*" * 50),"\n"
      "U kunt een keuze maken uit het volgende menu\n"
      "1 - Boek toevoegen\n"
      "2 - Boekenlijst opvragen \n"
      "3 - Boekenlijst per genre opvragen\n"
      "4 - Stoppen\n",
        ("*" * 50),"\n")


    keuze = int(input("Maak uw keuze: "))

    if keuze == 4:
        print("Tot ziens!")
        break
    elif keuze == 1:
        boek = input("Voer de titel van het boek in: ")
        auteur = input("Voer de naam van de auteur in: ")
        genre = input("Voer het genre in: ")
        publicatiejaar = input("Voer het jaar van publicatie in: ")

        bibliotheek[boek] = {
            "auteur": auteur,
            "genre": genre,
            "publicatiejaar": publicatiejaar
        }

        print(f'Het boek {boek} van {auteur} is toegevoegd aan de bibliotheek')
        print("*" * 50)

    elif keuze == 2:
        for boek in bibliotheek:
            print("*" * 50)
            print(f"Titel: {boek}")
            print(f"Auteur: {bibliotheek[boek]["auteur"]}")
            print(f"Genre: {bibliotheek[boek]["genre"]}")
            print(f"Publicatiejaar: {bibliotheek[boek]["publicatiejaar"]}")
    elif keuze == 3:
        genre = input("Voer het genre in: ")
        for boek in bibliotheek:
            if bibliotheek[boek]["genre"]== genre:
                print("*" * 50)
                print(f"Titel: {boek}")
                print(f"Auteur: {bibliotheek[boek]["auteur"]}")
                print(f"Genre: {bibliotheek[boek]["genre"]}")
                print(f"Publicatiejaar: {bibliotheek[boek]["publicatiejaar"]}")
                print("*" * 50)

    else:
        print("Verkeerde invoer, probeer het nog eens\n")



