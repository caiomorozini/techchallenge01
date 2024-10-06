from pydantic import BaseModel

class Processamento(BaseModel):
    ano: int
    subopcao: str
    categoria: str
    produto: str
    quantidade: float