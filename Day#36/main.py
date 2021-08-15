import requests
import html
from twilio.rest import Client

STOCK = ""
COMPANY_NAME = ""
API_KEY_S = ""
API_KEY_N = ""
account_sid = ""
auth_token = ""

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": 120,
    "apikey": API_KEY_S,
}
news_parameters = {
    "q": f"{COMPANY_NAME} stock",
    "apikey": API_KEY_N,
}

stock_url = 'https://www.alphavantage.co/query'
stock = requests.get(stock_url, params=stock_parameters)

news_url = "https://newsapi.org/v2/everything"
news = requests.get(news_url, params=news_parameters)

stock_dates = list(stock.json()["Time Series (Daily)"])[:2]
stock_data_today = float(
    stock.json()["Time Series (Daily)"][stock_dates[0]]["4. close"])
stock_data_yesterday = float(
    stock.json()["Time Series (Daily)"][stock_dates[1]]["4. close"])
stock_data_average = (
    (stock_data_yesterday - stock_data_today) * 100) / stock_data_today

msgs = []

if stock_data_average > 5:
    articles = news.json()['articles'][:3]
    for char in range(len(articles)):
        msg = msgs.append(html.unescape(f"{STOCK}: 🔺{round(stock_data_average)}%\n"
                                        f"Headline: {articles[char]['title']}\n"
                                        f"Brief: {articles[char]['content']}\n"))
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f"{msgs[0]}",
            from_='+19096717302',
            to='+16472078688'
        )
    print(message.status)
if stock_data_average < -5:
    articles = news.json()['articles'][:3]
    for char in range(len(articles)):
        msg = msgs.append(html.unescape(f"{STOCK}: ⬇ {round(stock_data_average)}%\n"
                                        f"Headline: {articles[char]['title']}\n"
                                        f"Brief: {articles[char]['content']}\n"))
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f"{msgs[0]}",
            from_='+19096717302',
            to='+16472078688'
        )
    print(message.status)
