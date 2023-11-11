import requests

def get_crypto_data():
    url = "https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"
    response = requests.get(url)
    if response.status_code == 200:
       return response.json()

crypto_response = get_crypto_data()

user_input = input("Enter your crypto currency : ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
        break


