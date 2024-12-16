# import requests
# import time

# def get_data():
#     # URL vortexic petq e texekutyuny vercnenq
#     url = 'https://api.coingecko.com/api/v3/coins/markets'
#     params = {
#         'vs_currency': 'usd',  # veradarcnum enq gnery
#         'order': 'market_cap_desc',  # sortavorum 
#         'per_page': 10,  # coinneri qanaky
#         'page': 1  # ejeri qanaky
#     }

#     # zapros kuxarkenq nshvac URL-in
#     response = requests.get(url, params)

#     # ete statusy 200 e uremn mez cuyc kta coini giny
#     if response.status_code == 200:
#         data = response.json()
#         # coini anuny u giny
#         for coin in data:
#             print(f"Coin: {coin['name']} ({coin['symbol']})")
#             print(f"Price: {coin['current_price']} USD")
#             print(f"Change in 24 hours: {coin['price_change_percentage_24h']}%\n")
#     elif response.status_code == 429:
#         # ete status kody 429 e uremn spasel 30 varkian u noric pordzel
#         print("ERROR 429: Request limit exceeded. Wait 30 seconds...")
#         time.sleep(30)  # spasel 30 varkian
#     else:
#         print(f"another ERROR: {response.status_code}")

# # anverj cikl amen 5 varkyany mek tvyalnery tarmacnelu hamar
# while True:
#     get_data()
#     time.sleep(5)