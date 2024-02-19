import pandas as pd 

data = pd.read_csv("data_alfabeto.csv") 

fonetica_dicc = {row.letter:row.code for (index, row) in data.iterrows()} 
print(fonetica_dicc) 
 
def generar_fonetica():
    palabra = input("Ingrese una palabra: ").upper()   
    try: 
        salida_lista = [fonetica_dicc[letter] for letter in palabra]  
    except KeyError:  
        print("Lo siento, solo letras del alfabeto por favor.")  
        generar_fonetica()
    else: 
        print(salida_lista) 
 
generar_fonetica()