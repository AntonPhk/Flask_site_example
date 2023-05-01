import requests


def get_bitcoin_price():
    resp = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
    bitcoin_price = resp.get('bitcoin', {}).get('USD')
    return bitcoin_price()