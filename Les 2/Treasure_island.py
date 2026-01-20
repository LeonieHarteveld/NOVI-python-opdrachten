# Je gaat een nieuw programma schrijven, genaamd Treasure.py. Dit programma is een spel waarbij de speler een aantal keuzes moet maken.
# Je mag zelf bepalen wat de keuzes zijn en wat de uitkomsten zijn van de keuzes. Het spel moet minimaal 4 verschillende keuzes bevatten.
# Het einde van het spel is een if elif else statement.
#
# Voorbeeld:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Rechts
#  Helaas heb je verkeerd gekozen en ben je in een gat gevallen. Game Over.
#
# Of:
# Welkom op het eiland van de schat.
# Je bent op een kruispunt, ga je links of rechts?
# Links
# Je komt bij een meer, ga je zwemmen of wachten?
# etc...




# Schrijf hier je code:


print(f"Welkom op het eiland van de schat. \n"
      f"Je komt op een kruising, aan de linker kant zie je gebergte en aan de rechterkant zie je de zee")

kruising = input("Ga je links of rechts?: ")

if kruising == "links":
    print("Je ziet een grot en een berg, welke kant ga je op?")
    kruising2 = input("Ga je naar de grot of berg?")
    if kruising2 == "grot":
        print("Je hebt de schat gevonden, Gefeliciteerd!")
        print("""
                          __..-----')
                ,.--._ .-'_..--...-'
               '-"'. _/_ /  ..--''""'-.
               _.--""...:._:(_ ..:"::. \\
            .-' ..::--""_(##)#)"':. \\ \\)    \\ _|_ /
           /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'
           "  / |  :' :/""\\///)  /:.'    --(       )--
             / :( :( :(   (#//)  "       .-'\\.___./'-.
            / :/|\\ :\\_:\\   \\#//\\            /  |  \\
            |:/ | ""--':\\   (#//)              '
            \\/  \\ :|  \\ :\\  (#//)
                 \\:\\   '.':. \\#//\\
                  ':|    "--'(#///)
                             (#///)
                             (#///)         ___/""\\     
                              \\#///\\           oo##
                              (##///)         `-6 #
                              (##///)          ,'`.
                              (##///)         // `.\\
                              (##///)        ||o   \\\\
                               \\##///\\        \\-+--//
                               (###///)       :_|_(/
                               (sjw////)__...--:: :...__
                               (#/::''':::     "" - -.._
                          __..-'''           __;: :            "-._
                  __..--""                  `---/ ;                '\\._
         ___..--""                             `-'                    "-..___
           (_ ""---....___                                     __...--"" _)
             ""--...  ___""'''-----......._______......----""'     --""
                                  ---.....   ___....----             
        """)
    else:
        print("Je hebt je verkeken, de berg houdt abrupt op en je valt in een ravijn.")
else:
    print("Je ziet een berg en de zee welke kant ga je op?")
    kruising3 = input("Ga je naar de berg of zee?")
    if kruising3 == "berg":
        print("Je hebt je verkeken, de berg houdt abrupt op en je valt in een ravijn.")
    else:
        print("Je rent de zee in, maar er blijken allemaal haaien te zitten. Helaas wordt je opgegeten door een mega jaws")
