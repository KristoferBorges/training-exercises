from fastapi import FastAPI

app = FastAPI()

estoque = {
    1: {"produto": "Arroz", "quantidade": 10, "valor": 10.00},
    2: {"produto": "Feijão", "quantidade": 5, "valor": 5.00},
    3: {"produto": "Macarrão", "quantidade": 7, "valor": 7.00},
    4: {"produto": "Carne", "quantidade": 15, "valor": 20.00},
    5: {"produto": "Frango", "quantidade": 20, "valor": 15.00},
    6: {"produto": "Peixe", "quantidade": 10, "valor": 25.00},
    7: {"produto": "Ovos", "quantidade": 30, "valor": 0.50},
    8: {"produto": "Leite", "quantidade": 10, "valor": 2.50},
    9: {"produto": "Café", "quantidade": 5, "valor": 5.00},
    10: {"produto": "Açucar", "quantidade": 5, "valor": 3.00},
    11: {"produto": "Sal", "quantidade": 5, "valor": 2.00},
    12: {"produto": "Óleo", "quantidade": 5, "valor": 5.00},
    13: {"produto": "Manteiga", "quantidade": 5, "valor": 5.00},
}

@app.get("/")
def home():
    return {"Estoque": len(estoque)}

@app.get("/estoque/{id_produto}")
def pegar_produto(id_produto: int):
    if id_produto in estoque:
        return estoque[id_produto]
    else:
        return {"Erro": "ID Produto inexistente"}