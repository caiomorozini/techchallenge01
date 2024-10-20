from pydantic import BaseModel, EmailStr

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

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None