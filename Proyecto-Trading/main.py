""" este código obtiene datos sobre el precio de cierre de una acción específica, calcula la diferencia porcentual entre el precio de cierre de ayer y  
el precio de cierre del día anterior, y si esa diferencia es significativa, busca noticias sobre la empresa asociada a esa acción y  
las envía como mensajes de texto utilizando Twilio """

import requests   
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything" 

STOCK_API_KEY = "FJ8PWONGKIOSFN9C"  
NEW_SAPI_KEY = "88a53984cc284a22ac6c9686f10f17aa" 
TWILIO_SID = "YOU SID" 
TWILIO_AUTH_TOKEN = "YOU TOKEN"

stock_params = {  
    "function": "TIME_SERIES_DAILY", 
    "symbol": STOCK_NAME, 
    "apikey": STOCK_API_KEY,
} 

response = requests.get(STOCK_ENDPOINT, params=stock_params)  
data = response.json()["Time Series (Daily)"] 
data_list = [value for (key, value) in data.items()]  
yesterday_data = data_list[0] 
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1] 
day_before_yesterday_price = day_before_yesterday_data["4. close"] 
print(day_before_yesterday_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_price)) 
print(difference)

difference_percent = round((difference / float(yesterday_closing_price)) * 100)
print(difference_percent)
 
if (difference_percen) > 1:  
    new_params = { 
            "apiKey": NEW_SAPI_KEY,  
            "q": COMPANY_NAME,
    }
     
    new_response = requests.get(NEWS_ENDPOINT, params=new_params) 
    articles = new_response.json()["articles"]  
    print(articles) 

    three_articles = articles[:3] 
    print(three_articles)


    formatted_articles = [f"{STOCK_NAME}:{difference_percent}%\Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles] 
     
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN) 
    
    for article in formatted_article:
        MESSAGE = client.messages.create(  
            body=article, 
            from_ = "YOUR NUMBER TWILIO", 
            to = "YOUR NUMBER CELL PHONE "

        )

