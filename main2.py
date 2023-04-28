import requests
import json

# Constants
SYMBOL = "IDR"
BASE = "CHF"
BOT_TOKEN = "YOUR_TELEGRAMBOT_TOKEN"
CHAT_ID = "YOUR_CHATBOT_ID"
FIXER_TOKEN = "YOUR_API_TOKEN"

def get_exchange_rate(symbol, base, fixer_token):
    url = f"https://api.apilayer.com/fixer/latest?symbols={symbol}&base={base}"
    headers = {"apikey": fixer_token}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        base_currency = response_dict["base"]
        exchange_rate = response_dict["rates"]
        return base_currency, exchange_rate
    else:
        raise Exception(f"Error fetching exchange rate data: {response.status_code}")

def send_telegram_message(bot_token, chat_id, text):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    response = requests.post(telegram_url)

    if response.status_code != 200:
        raise Exception(f"Error sending message via Telegram: {response.status_code}")

def main():
    try:
        base_currency, exchange_rate = get_exchange_rate(SYMBOL, BASE, FIXER_TOKEN)
        result_text = f"Exchange rate: {base_currency} to {list(exchange_rate.keys())[0]}: {exchange_rate[list(exchange_rate.keys())[0]]}"
        send_telegram_message(BOT_TOKEN, CHAT_ID, result_text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
