import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Stock api data fetching

stock_api_data = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=Api Key").json()['Time Series (Daily)']

stock_list = [value for key, value in stock_api_data.items()]
yesterday = stock_list[0]['4. close']

before_yesterday = stock_list[1]['4. close']

# Formatting data and checking percentage

difference = float(yesterday) - float(before_yesterday)
percent = (float(difference)/float(before_yesterday)) * 100
percentage = round(percent, 2)
percentage = 2
if percentage >= 0:
    if percentage > 0:
        print('ok')
        result = f'🔺{percentage}% \n\nDifference: {before_yesterday}$🔺{yesterday}$'
    else:
        print('not ok')
        result = f'🔻- {percentage}% \n\nDifference: {before_yesterday}$🔻{yesterday}$'

#News api data fetching

    date = datetime.date.today()
    CUSTOM_DATE = f"{date.year}-{date.month}-{date.day - 2}"
    news_api_data = requests.get(f'https://newsapi.org/v2/everything?'
           f'q={COMPANY_NAME}&'
           f'from={CUSTOM_DATE}&'
           'sortBy=popularity&'
           'Language=en&'
           'apiKey=3faec83fe62c4050aaefc40dd5a0f015').json()

    news = [value for key, value in news_api_data.items()]
    news_1 = (f"-------------------SHARES REPORT--------------------\n\nTSLA: {result} \n\nHEADLINE:"
              f" {news[2][0]['title']}...\nSHORT NEWS:"
              f" {news[2][0]['content']}...\n\n")
    news_2 = f"HEADLINE: {news[2][1]['title']}...\nSHORT NEWS: {news[2][1]['content']}...\n\n"
    news_3 = f"HEADLINE: {news[2][2]['title']}...\nSHORT NEWS: {news[2][2]['content']}..."
    total_news = news_1+news_2+news_3

# Twillio message connection

    account_sid = "Twillio Acoount Sid"
    auth_token = "Twillio Auth Token"
    client = Client (account_sid,
                     auth_token)

    message = client.messages.create (
        from_='whatsapp: Sender Number',
        body=total_news,
        to='whatsapp: Reciever Number'
    )

    print (message.sid)

