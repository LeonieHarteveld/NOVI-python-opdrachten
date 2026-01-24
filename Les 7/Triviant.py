import requests

def refactor_sentence(sentence):
    if '&' in sentence:
        sentence = sentence.replace('&quot;', '"') \
                           .replace('&#039;', "'") \
                           .replace('&amp;', '&') \
                           .replace('&lt;', '<') \
                           .replace('&gt;', '>')
    return sentence


def get_trivia_vraag():
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    response = requests.get(url)
    if response.ok:
        data = (response.json())
        vraag = (data["results"][0]["question"])
        vraag = refactor_sentence(vraag)

        correct_answer = data['results'][0]['correct_answer']
        incorrect_answers = data['results'][0]['incorrect_answers']
        options = incorrect_answers + [correct_answer]
        options.sort(reverse=True)
        return vraag, correct_answer, options
    else:
        print(f"Er is iets misgegaan. Status code: {response.status_code}")


def display_vraag(vraag, options):
    print("\n"+ vraag)
    for nummers, option in enumerate(options, start=1):
        print(f"{nummers}. {option}")

def get_user_answer():
    while True:
        keuze = input("Kies 1 of 2: ").strip()
        if keuze in ("1", "2"):
            return int(keuze)
        else:
            print("Ongeldige invoer. Typ 1 of 2.")









