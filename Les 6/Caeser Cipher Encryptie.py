# Caesar Cipher Encryptie/Decryptie
# Inleiding
# De Caesar Cipher is een eenvoudige vorm van substitutie-encryptie waarbij elke letter in de tekst wordt vervangen door een letter die een vast aantal posities later in het alfabet staat. Deze applicatie biedt een eenvoudige manier om tekst te versleutelen of te ontsleutelen met behulp van de Caesar Cipher. Julias Caesar heeft deze manier van encryptie zelf toegepast bij het versturen van belangrijke berichten.
#
# Het grootste nadeel van deze encrypter is dat er maar 25 mogelijkheden zijn dus een computer programma kan dit vrij simpel oplossen.
#
# Instructies
# Voer de gewenste actie in: encode (versleutelen) of decode (ontsleutelen).
# Voer de tekst in die je wilt versleutelen of ontsleutelen.
# Geef het aantal posities op waarmee je de letters wilt verschuiven (shift number).
# Het programma zal vervolgens de versleutelde of ontsleutelde tekst weergeven, afhankelijk van de opgegeven actie.
#
# Voorbeeld
# Type 'encode' to encrypt, type 'decode' to decrypt:
# encode
# Type your message:
# hello
# Type the shift number:
# 3
# the encoded text is: khoor
#
# Would you like to encrypt/decrypt again? (y/n)
# y
# Type 'encode' to encrypt, type 'decode' to decrypt:
# decode
# Type your message:
# khoor
# Type the shift number:
# 3
# the decoded text is: hello
#
# Would you like to encrypt/decrypt again? (y/n)
# n
# Thanks for using this application

# Aanvullende opmerkingen
# Deze Caesar Cipher implementatie ondersteunt alleen letters van het alfabet. Alle andere tekens blijven onveranderd.
# Als het aantal posities om te verschuiven groter is dan 26, zal het programma het verschuivingsaantal verminderen met 26 totdat het binnen het bereik van het alfabet valt.
# Je kunt het programma herhaaldelijk gebruiken totdat je ervoor kiest om te stoppen.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

"""Dit is het openings menu waarin de user input kan geven"""
def menu() :
    input_menu = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    return(input_menu)

''' Deze functie encode een invoer door te  zoeken naar de letters in de index en verschuift ze naar de gewenste shift '''
def encode () :
    woord_invoer = input("Schrijf je bericht: ")
    shift_nummer = int(input("Typ het shift nummer: "))
    resultaat = ""
    for letter in woord_invoer:
        if letter in alphabet:
            index = alphabet.index(letter)
            nieuw_letter = alphabet[(index + shift_nummer) % 26]
            resultaat += nieuw_letter
        else:
          resultaat += letter
    return resultaat

''' Deze functie decode een invoer door te  zoeken naar de letters in de index en verschuift ze naar de gewenste shift '''
def decode () :
    woord_invoer = input("Schrijf je bericht: ")
    shift_nummer = int(input("Typ het shift nummer: "))
    resultaat = ""
    for letter in woord_invoer:
        if letter in alphabet:
            index = alphabet.index(letter)
            nieuw_letter = alphabet[(index - shift_nummer) % 26]
            resultaat += nieuw_letter
        else:
            resultaat += letter
    return resultaat

"""De functie vraagt of je opnieuw wilt coderen"""
def while_functie():
    invoer = ""

    while True:
        invoer = input("Wil je opnieuw encrypten of decoderen? (y/n): ")
        if invoer == "y":
            return invoer
        elif invoer == "n":
            print("Bedankt en tot de volgende keer!")
            break
        else:
            print("Verkeerde invoer, probeer het nog eens")


def main():
    while True:
        keuze = menu()

        if keuze == "encode":
            print("the encoded text is:", encode())
        elif keuze == "decode":
            print("the decoded text is:", decode())
        else:
            print("Verkeerde keuze, typ 'encode' of 'decode'.")
            continue

        opnieuw = while_functie()
        if opnieuw == "n":
            break

main()





