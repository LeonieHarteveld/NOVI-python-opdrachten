# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small_pizza = 2
pepperoni = 3
kaas = 1

print("Welkom bij onze pizzaria. U kunt nu het formaat pizza bestellen")
pizza = (input("Wilt u small, medium of large?: "))

if pizza == "small":
    print("U heeft een small pizza gekozen")
    question_small_pepperoni = input("Wilt u peperoni op uw pizza? Y/N:")
    if question_small_pepperoni == "Y":
        kaas_small_pizza = input("Wilt u kaas op uw pizza? Y/N:")
        if kaas_small_pizza == "Y":
            print(f"Uw pizza is {small_pizza + pepperoni_small_pizza + kaas}euro")
        else:
            print(f"Uw pizza is {small_pizza + pepperoni_small_pizza}euro")
    else:
        kaas_small_pizza = input("Wilt u kaas op uw pizza? Y/N: ")
        if kaas_small_pizza == "Y":
            print(f"Uw pizza is {small_pizza + kaas}euro")
        else:
            print(f"Uw pizza is {small_pizza} euro")
elif pizza == "medium":
    print("U heeft een medium pizza gekozen")
    question_pepperoni = input("Wilt u peperoni op uw pizza? Y/N:")
    if question_pepperoni == "Y":
        kaas_pizza = input("Wilt u kaas op uw pizza? Y/N:")
        if kaas_pizza == "Y":
            print(f"Uw pizza is {medium_pizza + pepperoni + kaas}euro")
        else:
            print(f"Uw pizza is {medium_pizza + pepperoni}euro")
    else:
        kaas_pizza = input("Wilt u kaas op uw pizza? Y/N: ")
        if kaas_pizza == "Y":
            print(f"Uw pizza is {medium_pizza + kaas}euro")
        else:
            print(f"Uw pizza is {medium_pizza} euro")

else:
    print("U heeft een large pizza gekozen")
    question_pepperoni = input("Wilt u peperoni op uw pizza? Y/N:")
    if question_pepperoni == "Y":
        kaas_pizza = input("Wilt u kaas op uw pizza? Y/N:")
        if kaas_pizza == "Y":
            print(f"Uw pizza is {large_pizza + pepperoni + kaas}euro")
        else:
            print(f"Uw pizza is {large_pizza + pepperoni}euro")
    else:
        kaas_pizza = input("Wilt u kaas op uw pizza? Y/N: ")
        if kaas_pizza == "Y":
            print(f"Uw pizza is {large_pizza + kaas}euro")
        else:
            print(f"Uw pizza is {large_pizza} euro")


