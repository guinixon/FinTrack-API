from fastapi import FastAPI
from app.routes.financeiro_routes import router as financeiro_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Controle Financeiro")

#liberar o cors para tetes e desenvolvimento
app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)



app.include_router(financeiro_router)

@app.get("/")
def home():
    return{"mensagem":"Backend de Controle Financeiro com FastAPI "}