import requests as req
import datetime as dt
from twilio.rest import Client
def send_message(head,breif):
    twilio_sid="AC8f10bcdc572e41a07bf12878bd26da76"
    twilio_token="b499ef50d2133364befc2eaefef1afbc"
    client=Client(twilio_sid,twilio_token)
    client.messages \
       .create(
           body=f'{head}\n BREIF:{breif}',
           from_='+16812525263',
           to='+917598980499'
           )
def news(headdy):
    NEWS_API_key="096bc469eb284bd789a30e966e83ce21"
    datt = dt.datetime
    rr=req.get(url=f"https://newsapi.org/v2/everything?q=tesla&apiKey={NEWS_API_key}")
    headline=rr.json()["articles"]
    """this is to improve get news"""
    details=[headline[kk]["description"] for kk in range(0,3)]
    for i in range(3):
        send_message(headdy, details[i])

import itertools

daily: dict
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
re = []
alpha_api_key = "ZYMCMB7LHDW0YDV2"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=full&apikey={alpha_api_key}'
rrrr = req.get(url=url)
daily = rrrr.json()["Time Series (Daily)"]
yesterday_daybefore = dict(itertools.islice(daily.items(), 1, 3))


for i in yesterday_daybefore:
    value = yesterday_daybefore[i]['4. close']
    # print(f"{i}   {value}  ")
    re.append(float(value))
yesterday: float = re[0]
day_before = re[1]
percentage = (day_before / 100)


if ((percentage)*2) + day_before <yesterday:  # trigger  th
        he=u"TSLA \U0001F53A 2% \nHeadline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?."
        news(he)
if  day_before-((percentage)*5) >yesterday:
        he=u"TSLA:5 emoji:U+1F53A \ \nHeadline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?."
        news(he)

