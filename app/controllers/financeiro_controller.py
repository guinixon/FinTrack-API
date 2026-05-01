from app.database.mongo import transacoes_collection
from app.models.transacao_model import Transacao

def formatar_transacoes(transacao):
    transacao["_id"] = str(transacao["_id"])
    return transacao

def listar_transacoes():
    transacoes = list(transacoes_collection.find())
    return [formatar_transacoes(t) for t in transacoes]

def criar_transacoes(transacao: Transacao):
    dados = transacao.model_dump()
    resultado = transacoes_collection.insert_one(dados)
    nova_transacao = transacoes_collection.find_one(
        {"_id": resultado.inserted_id}
    )
    return formatar_transacoes(nova_transacao)

def calcular_saldo():
    transacoes = list(transacoes_collection.find())

    saldo = 0

    for t in transacoes:
        if t["tipo"] == "entrada":
            saldo+=t["valor"]
        else:
            saldo-=t["valor"]
    return {"saldo": saldo}

