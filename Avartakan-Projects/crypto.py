import requests
import time

def fetch_crypto_data(url, params):
    try:
        response = requests.get(url, params)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def process_response(response):
    if response is None:
        return

    if response.status_code == 200:
        data = response.json()
        display_crypto_data(data)
    elif response.status_code == 429:
        print("ERROR 429: Request limit exceeded. Waiting 30 seconds...")
        time.sleep(30)  
    elif response.status_code == 404:
        print("ERROR 404: Resource not found. Check the URL or endpoint.")
    elif response.status_code == 500:
        print("ERROR 500: Server error. Please try again later.")
    else:
        print(f"Unexpected ERROR: {response.status_code}")

def display_crypto_data(data):
    """Display cryptocurrency data in a readable format."""
    for coin in data:
        print(f"Coin: {coin['name']} ({coin['symbol']})")
        print(f"Price: {coin['current_price']} USD")
        print(f"Change in 24 hours: {coin['price_change_percentage_24h']}%\n")

def main():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1
    }

    while True:
        response = fetch_crypto_data(url, params)
        process_response(response)
        time.sleep(5)  

if __name__ == "__main__":
    main()
