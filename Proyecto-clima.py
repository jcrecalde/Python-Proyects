""" Cree un programa a traves de la API de twilio para avisar a traves de msj cuando llueve """  
""" Use pythoneverywhere para que todos los dias a las 7 AM envie alerta """ 
""" Cree un proxy para poder usar twilio con pythoneverywhere """
 
import requests  
import os
from twilio.rest import Client  
from twilio.http.http_client import TwilioHttpClient
 
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWN_API_KEY")    
account_sid = "Ingresar tu account sid"
auth_token = os.environ.get("OWN_AUTH_TOKEN")
 
weather_params = {  
    "lat": 47.262691, 
    "lon": 11.394700, 
    "appid": api_key, 
    "cnt": 4,

}

response = requests.get(weather_endpoint, params=weather_params)  
response.raise_for_status()
weather_data = response.json() 
#print(weather_data["list"][0]["weather"][0]["id"]) 
 
will_rain = False 
for hour_data in weather_data["list"]:  
    condition_code = hour_data["weather"][0]["id"] 
    if int(condition_code) < 700: 
        will_rain = True
if will_rain:  
    proxy_client = TwilioHttpClient() 
    proxy_client.session.proxies = {'https': os.environ[ 'https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client) 
    message = client.messages \
                .create(
                     body="Va a llover hoy. Recuerda llevar paraguas!",
                     from_='+19252755183',
                     to='+542284607211'
    ) 
    print(message.status)