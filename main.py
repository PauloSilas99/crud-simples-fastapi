from fastapi import FastAPI,HTTPException # "HTTPException" usada para retornar erros HTTP
from modelo_dados import Item
from typing import List # tipos de dados que vou usar para definir entrada e saída da Api

app = FastAPI()

items = [] # banco de dados em memória

#Criar um novo item
# Obs: O (item: Item) valida a entrada da requisição, enquanto o response_model=Item valida e serializa a saída (resposta)
# "response_model" modelo de dados que será retornado como resposta

@app.post("/items/", response_model = Item) 
def create_item(item:Item):
    items.append(item)
    return item

@app.get("/items/", response_model= List[Item])
def get_items():
    return items

#Ler um item específico pelo Id
@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id:int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404,detail="Item not found")    

#Atualizar um item específico
@app.put("/items/{item_id}", response_model= Item)
def update_item(item_id: int, update_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = update_item
            return update_item
    raise HTTPException(status_code=404,detail="Item not found")    

#Deletar um item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")