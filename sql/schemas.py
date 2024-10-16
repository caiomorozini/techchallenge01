from pydantic import BaseModel

class Producao(BaseModel):
    class Config:
        from_attributes = True
    
class Processamento(BaseModel):
    class Config:
        from_attributes = True

class Comercializacao(BaseModel):
    class Config:
        from_attributes = True

class Importacao(BaseModel):
    class Config:
        from_attributes = True

class Exportacao(BaseModel):
    class Config:
        from_attributes = True