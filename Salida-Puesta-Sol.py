"""obtener la posición actual de la Estación Espacial Internacional (ISS) y la API de Sunrise Sunset para obtener la información sobre el amanecer y el atardecer en una ubicación específica""" 
 
import requests 
from datetime import datetime 
import smtplib
  
MY_EMAIL = "Ingresar email" 
MY_CONTRASEÑA = "Ingresar contraseña"
MY_LAT = -36.887409 
MY_LONG = -60.315201 
 
def comprobacion():
    response = requests.get(url="http://api.open-notify.org/iss-now.json") 
    response.raise_for_status() 
    data = response.json() 
 
    es_latitud = float(data["iss_position"]["latitude"]) 
    es_longitud = float(data["iss_position"]["longitude"]) 

    if MY_LAT-5 <= es_latitud <= MY_LAT+5 and MY_LONG-5 <= es_longitud <= MY_LONG+5:  
        return True
 
def es_noche(): 

    parametros = { 
        "lat": MY_LAT, 
        "long": MY_LONG, 
        "formatted": 0,
        }   

    response = requests.get("https://api.sunrise-sunset.org/json", params=parametros) 
    response.raise_for_status() 
    data = response.json() 
    salida_sol = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    puesta_sol = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    tiempo_ahora = datetime.now().hour
    
    if tiempo_ahora >= salida_sol or tiempo_ahora <= puesta_sol:  
        return True 
 
if comprobacion() and es_noche():  
    conexion = smtplib.SMTP("smtp.gmail.com") 
    conexion.starttls() 
    conexion.login(MY_EMAIL, MY_CONTRASEÑA) 
    conexion.sendemail( 
        from_addr=MY_EMAIL, 
        to_addres=MY_EMAIL, 
        msg="Buscar\n\n La ISS esta por encima de tu en el cielo"
    )

