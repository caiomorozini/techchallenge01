from pydantic import BaseModel

class Importacao(BaseModel):
    ano: int
    subopcao: str
    pais: str
    quantidade = float
    valor: float