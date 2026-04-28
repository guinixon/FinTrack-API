from fastapi import FastAPI
from app.routes.financeiro_routes import router as financeiro_router

app = FastAPI(title="FinTrack")

app.include_router(financeiro_router)

@app.get("/")
def home():
    return{"mensagem":"Backend de Controle Financeiro com FastAPI "}