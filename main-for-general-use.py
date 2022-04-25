import requests
import datetime
from twilio.rest import Client


NEWS_API_KEY = "YOUR NEWSAPI.CO KEY HERRE"
STOCK_API_KEY = "YOUR ALPHAVANTAGE KEY HERE"
account_sid = 'YOUR TWILIO SID HERE'
auth_token = 'YOUR TWILIO TOKEN HERE'
automatedPhoneNumber="YOUR TWILIO NUMBER HERE"
myPhoneNumber="YOUR PERSONAL PHONE NUMBER HERE"

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_PARAMETERS={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"60min",
    "apikey":STOCK_API_KEY
}

response=requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS).json()

today=datetime.datetime.now().date()
yesterday=str(today-datetime.timedelta(days=1))
ereyester=str((today-datetime.timedelta(days=2)))

yesterValue=float(response["Time Series (Daily)"][yesterday]['4. close'])
ereyesterValue=float(response["Time Series (Daily)"][ereyester]['4. close'])


stockChange=(yesterValue-ereyesterValue)/ereyesterValue *100

if abs(stockChange) >=5:

    NEWS_PARAMETERS={
            "from":yesterday,
            "q":COMPANY_NAME,
            "searchIn":"title",
            "sortBy":"popularity",
            "pageSize":3,
            "language":"en",
            "apikey":NEWS_API_KEY
        }

    newsResponse=requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS).json()["articles"]

    if stockChange>0:
        messageStart=f"{STOCK} 🔺 {abs(round(stockChange,2))}% !"
        print(messageStart)

    else:
        messageStart = f"{STOCK} 🔻 {abs(round(stockChange, 2))}% !\n\n"
        print(messageStart)


    headingsList=["\nheadline:"+x["title"]+"\nBreif:"+x["description"] for x in newsResponse]
    messageBody='\n'.join(headingsList)
    print(messageBody)

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=messageStart+ messageBody, from_=automatedPhoneNumber, to=myPhoneNumber)

