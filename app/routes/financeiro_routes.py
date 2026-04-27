from fastapi import APIRouter
from app.controllers.financeiro_controller import (
    listar_transacoes,
    criar_transacoes,
    calcular_saldo
)
from app.models.transacao_model import Transacao

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])

@router.get("/transacoes")
def get_transacoes():
    return listar_transacoes()

@router.post("/transacoes")
def post_transacao(transacao: Transacao):
    return criar_transacoes(transacao)

@router.get("/saldo")
def get_saldo():
    return calcular_saldo()