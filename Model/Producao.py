from pydantic import BaseModel

class Producao(BaseModel):
    ano: int
    categoria: str
    produto: str
    quantidade = float