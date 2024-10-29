from sqlalchemy.orm import Session
from Util import Contantes
from sqlalchemy import select

from Util.Security import get_password_hash
from . import models, schemas

#=========================================================================================================================================================================
#Producao
def check_producao_exists(db: Session, ano: int) -> bool:
    # Realiza a consulta para verificar se existe algum dado para o ano especificado
    return db.query(models.Producao).filter(models.Producao.ano == ano).first() is not None

def get_dados_producao(db: Session, ano: int):
    if check_producao_exists(db, ano):
        return db.query(models.Producao).filter(models.Producao.ano == ano).all()
    else:
        raise Exception()

def insert_dados_producao(db: Session, lista_producao: list):
    lista_db_prod = list()
    if len(lista_producao) > 0:
        db.query(models.Producao).filter(models.Producao.ano == lista_producao[0].ano).delete()
        db.commit()
    for dado in lista_producao:
        db_producao = models.Producao(ano = dado.ano, categoria = dado.categoria, produto = dado.produto, quantidade = dado.quantidade)
        lista_db_prod.append(db_producao)
    db.add_all(lista_db_prod)
    db.commit()
    return lista_db_prod
#=========================================================================================================================================================================
#Processamento
def check_processamento_exists(db: Session, ano: int, subopcao: Contantes.SubOpcoesProc) -> bool:
    # Realiza a consulta para verificar se existe uma registro com o ano especificado
    return db.query(models.Processamento).filter(models.Processamento.ano == ano, models.Processamento.subopcao == subopcao.value).first() is not None

def get_dados_processamento(db: Session, ano: int, subopcao: Contantes.SubOpcoesProc):
    if check_processamento_exists(db, ano, subopcao):
        return db.query(models.Processamento).filter(models.Processamento.ano == ano, models.Processamento.subopcao == subopcao.value).all()
    else:
        return Exception()

def insert_dados_processamento(db: Session, lista_processamento: list):
    lista_db_proc = list()
    if len(lista_processamento) > 0:
        db.query(models.Processamento).filter(models.Processamento.ano == lista_processamento[0].ano, models.Processamento.subopcao == lista_processamento[0].subopcao).delete()
        db.commit()
    for dado in lista_processamento:
        db_processamento = models.Processamento(ano = dado.ano, subopcao = dado.subopcao, categoria = dado.categoria, produto = dado.produto, quantidade = dado.quantidade)
        lista_db_proc.append(db_processamento)
    db.add_all(lista_db_proc)
    db.commit()
    return lista_db_proc
#=========================================================================================================================================================================
#Comercializacao
def check_comercializacao_exists(db: Session, ano: int) -> bool:
    # Realiza a consulta para verificar se existe um registro com o ano especificado
    return db.query(models.Comercializacao).filter(models.Comercializacao.ano == ano).first() is not None

def get_dados_comercializacao(db: Session, ano: int):
    if check_comercializacao_exists(db, ano):
        return db.query(models.Comercializacao).filter(models.Comercializacao.ano == ano).all()
    else:
        return Exception()

def insert_dados_comercializacao(db: Session, lista_comercializacao: list):
    lista_db_come = list()
    if len(lista_comercializacao) > 0:
        db.query(models.Comercializacao).filter(models.Comercializacao.ano == lista_comercializacao[0].ano).delete()
        db.commit()
    for dado in lista_comercializacao:
        db_comercializacao = models.Comercializacao(ano = dado.ano, categoria = dado.categoria, produto = dado.produto, quantidade = dado.quantidade)
        lista_db_come.append(db_comercializacao)
    db.add_all(lista_db_come)
    db.commit()
    return lista_db_come
#=========================================================================================================================================================================
#Importacao
def check_importacao_exists(db: Session, ano: int, subopcao: Contantes.SubOpcoesImport) -> bool:
    # Realiza a consulta para verificar se existe uma registro com o ano especificado
    return db.query(models.Importacao).filter(models.Importacao.ano == ano, models.Importacao.subopcao == subopcao.value).first() is not None

def get_dados_importacao(db: Session, ano: int, subopcao: Contantes.SubOpcoesImport):
    if check_importacao_exists(db, ano, subopcao):
        return db.query(models.Importacao).filter(models.Importacao.ano == ano, models.Importacao.subopcao == subopcao.value).all()
    else:
        return Exception()

def insert_dados_importacao(db: Session, lista_importacao: list):
    lista_db_imp = list()
    if len(lista_importacao) > 0:
        db.query(models.Importacao).filter(models.Importacao.ano == lista_importacao[0].ano, models.Importacao.subopcao == lista_importacao[0].subopcao).delete()
        db.commit()
    for dado in lista_importacao:
        db_importacao = models.Importacao(ano = dado.ano, subopcao = dado.subopcao, pais = dado.pais, quantidade = dado.quantidade, valor = dado.valor)
        lista_db_imp.append(db_importacao)
    db.add_all(lista_db_imp)
    db.commit()
    return lista_db_imp
#=========================================================================================================================================================================
#Exportacao
def check_exportacao_exists(db: Session, ano: int, subopcao: Contantes.SubOpcoesExport) -> bool:
    # Realiza a consulta para verificar se existe uma registro com o ano especificado
    return db.query(models.Exportacao).filter(models.Exportacao.ano == ano, models.Exportacao.subopcao == subopcao.value).first() is not None

def get_dados_exportacao(db: Session, ano: int, subopcao: Contantes.SubOpcoesExport):
    if check_exportacao_exists(db, ano, subopcao):
        return db.query(models.Exportacao).filter(models.Exportacao.ano == ano, models.Exportacao.subopcao == subopcao.value).all()
    else:
        return Exception()

def insert_dados_exportacao(db: Session, lista_exportacao: list):
    lista_db_exp = list()
    if len(lista_exportacao) > 0:
        db.query(models.Exportacao).filter(models.Exportacao.ano == lista_exportacao[0].ano, models.Exportacao.subopcao == lista_exportacao[0].subopcao).delete()
        db.commit()
    for dado in lista_exportacao:
        db_exportacao = models.Exportacao(ano = dado.ano, subopcao = dado.subopcao, pais = dado.pais, quantidade = dado.quantidade, valor = dado.valor)
        lista_db_exp.append(db_exportacao)
    db.add_all(lista_db_exp)
    db.commit()
    return lista_db_exp
#=========================================================================================================================================================================
#USUARIOS
#=========================================================================================================================================================================
def get_dados_usuario(user:schemas.UserSchema, db: Session):
    db_user = db.scalar(
        select(models.User).where((models.User.username == user.username) | (models.User.email == user.email))
        )
    return(db_user)
#=========================================================================================================================================================================
def get_dados_usuario_userid(id:int, db: Session):
    db_user = db.scalar(
        select(models.User).where((models.User.id == id))
        )
    return(db_user)
#=========================================================================================================================================================================
def get_dados_usuario_email(email:str, db: Session):
    db_user = db.scalar(
        select(models.User).where((models.User.email == email))
        )
    return(db_user)
#=========================================================================================================================================================================
def insert_dados_usuario(user:schemas.UserSchema, db: Session):
    hash_pass = get_password_hash(user.password)
    db_user = models.User(
        username=user.username, password=hash_pass, email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return  db_user
#=========================================================================================================================================================================
def delete_dados_usuario(db_user:models.User, db: Session):
    db.delete(db_user)
    db.commit()
    return
#=========================================================================================================================================================================