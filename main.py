from fastapi import FastAPI
from anthropic import Anthropic
import os

app = FastAPI()

cliente = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.post("/consultar")
def consultar_jurisbot(mensaje: dict):
    texto_usuario = mensaje.get("pregunta")
    
    respuesta = cliente.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        system="Eres JurisBot, un asistente legal experto en derecho laboral en Chile. Responde de forma clara y profesional.",
        messages=[{"role": "user", "content": texto_usuario}]
    )
    
    return {"respuesta_legal": respuesta.content[0].text}
