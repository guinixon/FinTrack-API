from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["controle_financeiro"]

transacoes_collection = db["transacoes"]