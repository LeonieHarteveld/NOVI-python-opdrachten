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
    url = "https://opentdb.com/api.php?amount=1&type=boolean"
    response = requests.get(url)
    if response.ok:
        data = (response.json())
        vraag = (data["results"][0]["question"])
        vraag = refactor_sentence(vraag)
        return vraag


print(get_trivia_vraag())








