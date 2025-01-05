import requests
import json
import os
import sys

user_input = input("Weather(1), Currency Coversion(2), Crypto Price(3): ")


if user_input == "1":
    city_name = input("city name:  ")
    def weather_api():
        try:
            with open("wea.json", "r") as file:
                weather = json.load(file)
                return weather.get("api_key", "error") 
        except FileNotFoundError as e:
            print(e)
    api_key = weather_api()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url, timeout=5)
    except TimeoutError as e:
        print(e)
    
    if response.status_code == 200:
        data = response.json()
        
        cityname = data["name"]
        temperture = data["main"]["temp"]
        feels = data["main"]["feels_like"]

        temperture_f = 1.8 * (temperture - 273.15) + 32
        temf_rounded = round(temperture_f)

        feels_f = 1.8 * (feels - 273.15) + 32
        feels_round_f = round(feels_f)

        print(f"the temperture in {cityname}")
        print(f"{temf_rounded}°F")
        print(f"feels like {feels_round_f}°F")
    else:
        print(ConnectionError)

elif user_input == "2":

    amount = float(input("amount: "))
    currencry1 = input("first currencry: ").upper()
    currencry2 = input("second currency: ").upper()

    def get_api():    
        try:
            with open("convert.json", 'r') as file:
                dat = json.load(file)
                return dat.get("api_key", [])
        except FileNotFoundError as e:
            print(e)

    api_key = get_api()

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currencry1}"    

    try:
        response = requests.get(url, timeout=5)
    except TimeoutError as e:
    
        print(e)
    except ConnectionError as e:
        print(e)
    except Exception as e:
        print(e)

    if response.status_code == 200:
        data = response.json()

        conversion_rates = data["conversion_rates"]

        get_curr = conversion_rates[currencry2]

        calc = amount * get_curr

        print(f"{amount} {currencry1} is {calc} {currencry2}")

    else:
        print(requests.exceptions.ConnectionError)

elif user_input == "3":

    def get_price(coin_symbol):
        
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_symbol}&vs_currencies=usd'

        try:
            response = requests.get(url, timeout=5)
        except ConnectionError as e:

            print(e)
        except TimeoutError as e:

            print(e)

        except Exception as e:
            print(e)
        
        if response.status_code == 200:
            data = response.json()

            coin = data[coin_symbol]["usd"]

            print(f"{coin_symbol} is $ {coin}")

            amount = input("amount: ")

            while True:
                if amount == "":
                    sys.exit()
                    break
                else:
                    math = float(amount) * coin
                    print(f"$ {math}")
                    sys.exit()
                    break
        else:
            print(ConnectionError)        

    def main():
        user_input = input("coin name: ").strip().lower()

        get_price(user_input)

    
    if __name__ == "__main__":
        print("please enter the coins name")
        main()
