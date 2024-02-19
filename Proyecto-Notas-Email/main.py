import smtplib    
import datetime as dt 
import random
 
""" El password debe ser generado a traves de verificacion de 2 pasos a traves de su email. """

my_email = "jcrecalde30@gmail.com" 
password = "ibayjlsbggyqrnnv"

hora_actual = dt.datetime.now()  
dia_semana = hora_actual.weekday() 
if dia_semana == 1: 
    with open(data_fraces, "r") as fraces: 
        contenido = fraces.readlines()
        frase_random = random.choice(contenido)   
 
    with smtplib.SMTP("smtp.gmail.com") as coneccion:
        conexion.starttls()  
        conexion.login(user=my_email, password=password) 
        conexion.sendmail( 
            from_addr=my_email,  
            to_addrs="jrecalde65@yahoo.com",  
            msg=f"Subject:Hello, this is today's phrase of the day\n\n.{frase_random}" 
        ) 
        conexion.close() 


