from fastapi import FastAPI

app = FastAPI(
    title="Agente Virtual",
    description="API para automatización de mensajes y gestión de citas",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Agente Virtual funcionando"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok"
    }

