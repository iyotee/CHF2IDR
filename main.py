import requests

TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_USERID"
EXCHANGE_RATE_API_KEY = "YOUR EXCHANGERATE-API.COM TOKEN"


def get_exchange_rate(from_currency, to_currency):
    url = "https://api.exchangerate-api.com/v4/latest/{}".format(from_currency)
    response = requests.get(url, {"api_key": EXCHANGE_RATE_API_KEY})
    response_json = response.json()
    exchange_rate = response_json["rates"][to_currency]
    return exchange_rate


def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount


def send_message(text):
    url = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, json=payload)


# Example usage: convert 1 CHF to IDR
amount = 1
from_currency = "CHF"
to_currency = "IDR"
converted_amount = convert_currency(amount, from_currency, to_currency)
send_message("{} {} is {} {}".format(
    amount, from_currency, converted_amount, to_currency))
