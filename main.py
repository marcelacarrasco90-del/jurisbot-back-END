from fastapi import FastAPI
from anthropic import Anthropic
import os

# Esto crea tu servidor
app = FastAPI()

# Esto prepara a Claude usando tu llave secreta
cliente = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Esta es la "puerta" por donde tu app enviará las preguntas
@app.post("/consultar")
def consultar_jurisbot(mensaje: dict):
    texto_usuario = mensaje.get("pregunta")
    
    # Aquí llamamos a Claude
    respuesta = cliente.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        system="Eres JurisBot, un asistente legal experto en derecho laboral en Chile. Responde de forma clara y profesional.",
        messages=[{"role": "user", "content": texto_usuario}]
    )
    
    # Devolvemos la respuesta a tu app
    return {"respuesta_legal": respuesta.content[0].text}
