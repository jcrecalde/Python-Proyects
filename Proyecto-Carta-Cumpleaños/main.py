from datetime import datetime 
import pandas as pd 
import random 
import smtplib   

""" Utilice pythonanywhere para que que programe y envie atumaticamente los email de cumpleaños."""

mi_email = "jcrecalde30@gmail.com" 
mi_contraseña = "Tu contraseña de verificacion a 2 pasos"

hoy = datetime.now() 
hora_tupla = (hoy.mes, hoy.dia) 

data = pd.read_csv("cumpleaños.csv")
cumpleaños_dic = {(data_fila["mes"], data_fila["dia"]): data_fila for (index, data_fila) in data.iterrows()} 

if hora_tupla in cumpleaños_dic:  
    persona_cumpleaños = cumpleaños_dic[hora_tupla]
    ruta_archivo = f"cartas_templates/{random.randint(1, 3)}.text" 
    with open(ruta_archivo) as carta_archivo: 
        contenido = carta_archivo.read() 
        contenido = contenido.replace("[NOMBRE]", persona_cumpleaños["nombre"]) 
     
    with smtplib.SMTP(smtp.gmail.com) as conexion: 
        conexion.starttls() 
        conexion.login(mi_email, mi_contraseña) 
        conexion.sendmail( 
            from_addr=mi_email,  
            to_addrs=persona_cumpleaños["email"],   
            msg=f"Subject: Feliz Cumpleaños!\n\n{contenido}"
        )