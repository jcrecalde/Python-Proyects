data_preguntas = [
    {"text": "La sangre de una babosa es verde.", "respuesta": "True"},
    {"text": "El animal más ruidoso es el elefante africano.", "respuesta": "False"},
    {"text": "Aproximadamente una cuarta parte de los huesos humanos se encuentran en los pies.", "respuesta": "True"},
    {"text": "La superficie total de los pulmones humanos es del tamaño de un campo de fútbol.",
        "respuesta": "True"},
    {"text": "En Virginia Occidental, EE. UU., si accidentalmente golpeas a un animal con tu automóvil, puedes llevártelo a casa para comer.", "respuesta": "True"},
    {"text": "En Londres, Reino Unido, si mueres en la Casa del Parlamento, tienes derecho a un funeral de estado.", "respuesta": "False"},
    {"text": "En Portugal es ilegal orinar en el océano.", "respuesta": "True"},
    {"text": "Puedes llevar a una vaca por las escaleras pero no por las escaleras.",
        "respuesta": "False"},
    {"text": "Google originalmente se llamaba 'Backrub'.", "respuesta": "True"},
    {"text": "El apellido de soltera de la madre de Buzz Aldrin era 'Moon'.",
        "respuesta": "True"},
    {"text": "Ningún trozo de papel cuadrado seco se puede doblar por la mitad más de 7 veces.",
        "respuesta": "False"},
    {"text": "Unas onzas de chocolate pueden matar a un perro pequeño.", "respuesta": "True"}
]

class Preguntas:  
    def __init__(self, p_text, p_respuesta): 
        self.text = p_text 
        self.respuesta = p_respuesta 
 


class prueba_pregunta:

    def __init__(self, p_list): 
        self.pregunta_numero = 0  
        self.puntuacion = 0 
        self.pregunta_lista = p_list  
     

    def aun_tienes_preguntas(self): 
        return self.pregunta_numero < len(self.pregunta_lista)
     
     
    def siguiente_pregunta(self):   
        actual_pregunta = self.pregunta_lista[self.pregunta_numero]  
        self.pregunta_numero += 1
        usuario_respuesta= input(f"Q.{self.pregunta_numero}: {actual_pregunta.text} (True/False)")  
        self.comprobar_respuesta(usuario_respuesta, actual_pregunta.respuesta)
     
    def comprobar_respuesta(self, usuario_respuesta, respuesta_correcta):     
        if usuario_respuesta.lower() == respuesta_correcta.lower():  
            self.puntuacion += 1
            print("Lo hiciste bien!!! =D")
        else: 
            print("Eso esta mal!!! =(") 
        print(f"La respuesta correcta es: {respuesta_correcta}") 
        print(f"Tu puntuacion actual es: {self.puntuacion}/{self.pregunta_numero}") 
        print("\n")


        


banco_preguntas = []
for preguntas in data_preguntas:
    pregunta_text = preguntas["text"]
    pregunta_respuesta = preguntas["respuesta"]
    nueva_pregunta = Preguntas(pregunta_text, pregunta_respuesta)
    banco_preguntas.append(nueva_pregunta) 
 
 
 
prueba = prueba_pregunta(banco_preguntas) 
 
while prueba.aun_tienes_preguntas():
    prueba.siguiente_pregunta() 
     
print("Completaste las preguntas")  
print(f"Tu puntuacion final es: {prueba.puntuacion}/{prueba.pregunta_numero}")
    
