from pydantic import BaseModel

class Exportacao(BaseModel):
    ano: int
    subopcao: str
    pais: str
    quantidade: float
    valor: float