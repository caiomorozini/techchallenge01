from pydantic import BaseModel

class Producao(BaseModel):
    class Config:
        orm_mode = True
    
class Processamento(BaseModel):
    class Config:
        orm_mode = True

class Comercializacao(BaseModel):
    class Config:
        orm_mode = True

class Importacao(BaseModel):
    class Config:
        orm_mode = True

class Exportacao(BaseModel):
    class Config:
        orm_mode = True