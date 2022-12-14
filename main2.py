import requests
import json

symbol = "IDR"
base = "CHF"
bot_token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
chat_id = "YOUR_CHAT_ID_HERE"
fixer_token = "YOUR_FIXER.IO_OR_APILAYER_API_KEY"

url = "https://api.apilayer.com/fixer/latest?symbols={}&base={}".format(
    symbol, base)

payload = {}
headers = {
    "apikey": fixer_token
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

# Parse the JSON string into a dictionary
response_dict = json.loads(response.text)

# Access the values of the dictionary
base_currency = response_dict["base"]
exchange_rate = response_dict["rates"]

# Format the values into a plain text string
result_text = f"Exchange rate: {base_currency} to {exchange_rate}"

if (status_code == 200):
    # Send the result in a telegram user
    telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(bot_token, chat_id, result_text)
    requests.post(telegram_url)
