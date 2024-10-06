from pydantic import BaseModel

class Comercializacao(BaseModel):
    ano: int
    categoria: str
    produto: str
    quantidade = float