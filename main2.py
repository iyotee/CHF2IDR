import requests
import json

symbol = "IDR"
base = "CHF"

url = "https://api.apilayer.com/fixer/latest?symbols={}&base={}".format(
    symbol, base)

payload = {}
headers = {
    "apikey": "7IX8d8YBCh1d63pbLd7r0TyO4kmX9DhF"
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
    telegram_url = f"https://api.telegram.org/bot5925869792:AAETkfiEIJ5VBbSHW7vzygzfqDpHOKTZBxA/sendMessage?chat_id=1011416325&text={result_text}"
    requests.post(telegram_url)
