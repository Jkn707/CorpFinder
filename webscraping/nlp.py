from dotenv import load_dotenv
from openai import OpenAI
import os

_ = load_dotenv('openAI.env')
client   = OpenAI(api_key=os.environ.get('openAI_api_key'),)

def obtenerEmociones(comentario):
    respuesta = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=(f"Analisis sentimental, dando solo una respuesta, Positivo, Negativo o Neutral de el sigiente texto: '{comentario}'"),
    )
    emocion = respuesta.choices[0].text.strip()   
    return(emocion)
    
    

      
         