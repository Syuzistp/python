# import requests

# def provide_joke():
#     # ays funkciayum mer url-i mijocov mez katak e tramadrvum 
#     url = "https://official-joke-api.appspot.com/random_joke"
#     response = requests.get(url)
    
#     # ete status code-y 200 e apa json-i mijocov kataky 2 maseri e bajanvum 
#     if response.status_code == 200:
#         joke = response.json()
#         return joke['setup'], joke['punchline']
#     # ete zaprosy chi stacvum stanum enq None
#     else:
#         print("Fail")
#         return None, None

# def rate_joke(setup, punchline):
#     # ays funkciayov gnahatum enq kataky
#     print(setup)
#     print(punchline)
#     rating = int(input("Rate joke 1-10: "))
#     return rating
    
# def jokes_file(jokes):
#     # ays funkciayov kataky pahpanum enq file-i mej ev sortavorum yst mer tvac gnahatakani
#     sorted_jokes = sorted(jokes, key=lambda x: x[0], reverse=True)
    
#     with open("random_joke.txt", "w") as file:
#         for rating, setup, punchline in sorted_jokes:
#             file.write(f"Rating: {rating}\n")
#             file.write(f"{setup}\n")
#             file.write(f"{punchline}\n\n")

# def main():
#     jokes = []
    
#     # mez tramadrum e 10 katak
#     for i in range(10):
#         setup, punchline = provide_joke()
#         if setup and punchline:
#             rating = rate_joke(setup, punchline)
#             jokes.append((rating, setup, punchline))

#     jokes_file(jokes)

# main()