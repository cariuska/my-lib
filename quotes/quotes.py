import requests

def get_quotes():
    req = requests.get("https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes")
    return req.json()

def get_quote(quote_number):
    req = requests.get(f"https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/{quote_number}")
    return req.json()