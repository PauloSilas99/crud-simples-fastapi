from pydantic import BaseModel # usada para definir os modelos de dados que vou manipular
from typing import Optional # tipos de dados que vou usar para definir entrada e saída da Api

class Item(BaseModel):
    name: str
    description : Optional[str] = None
    price: float
    on_offer: bool = False # indica se o item está em oferta