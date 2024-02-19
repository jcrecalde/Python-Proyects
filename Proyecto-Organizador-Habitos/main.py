import requests   
from datetime import datetime

USERNAME = "juancr" 
TOKEN = "jksajksahkhjfllglhkjkhk" 
GRAPH_ID = "graph1"

pixels_endpoint = "https://pixe.la/v1/users" 
  
""" Crear usuario pixel"""
users_params = {  
    "token": TOKEN,   
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes",

}
 
""" Creada la cuenta lo comentamos para que no genere errores al ejecutar """
#response = requests.post(url=pixels_endpoint, json=users_params) 
#print(response.text)   

""" Crear grafico"""
graph_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs" 

""" Solicitud """  
graph_config = { 
    "id": GRAPH_ID, 
    "name": "Runing Graph", 
    "unit": "Km", 
    "type": "float", 
    "color": "ajisai"
}  

headers= { 
    "X-USER-TOKEN": TOKEN,
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) 
#print(response.text) 

pixel_creation_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"  
 
today = datetime.now()

pixel_data = { 
    "date": today.strftime("%Y%m%d"), 
    "quantity": input("how many kilometers did you cicle today? "),
} 

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers) 
print(response.text) 

update_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}" 

new_pixel_data = { 
    "quantity": "4",
} 

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers) 
#print(response.text)

delete_endpoint = f"{pixels_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
 
#response = requests.delete(url=delete_endpoint, headers=headers) 
#print(response.text)