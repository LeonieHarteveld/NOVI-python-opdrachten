import requests
from API_key import API_KEY

def get_eur_to_usd_rate():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR"
    response = requests.get(url)

    if response.ok:
        data = response.json()

        if "USD" in data["conversion_rates"]:
            return data["conversion_rates"]["USD"]
        else:
            print("Fout: USD wisselkoers niet gevonden.")
            return None


    else:
        print(f"Fout: {response.status_code} - {response.text}")
        return None

def convert_eur_to_usd(amount, exchange_rate):
    return amount * exchange_rate

def user_input() :
    eur_input = float(input("Voer het bedrag in EUR in: "))
    return eur_input

def main():
    result =  convert_eur_to_usd(user_input(), get_eur_to_usd_rate())
    print(f"Bedrag in USD: {result}")


main()




