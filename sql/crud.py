from sqlalchemy.orm import Session
from Util import Contantes
from . import models, schemas

#Producao
def get_producao(db: Session, ano: int):
    return db.query(models.Producao).filter(models.Producao.ano == ano)

def get_producao_all(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Producao).offset(skip).limit(limit).all()

def create_producao(db: Session, producao: schemas.Producao):
    db_producao = models.Producao(ano = producao.ano, categoria = producao.categoria, produto = producao.produto, quantidade = producao.quantidade)
    db.delete(db_producao)
    db.add(db_producao)
    db.commit()
    db.refresh(db_producao)
    return db_producao

#Processamento
def get_processamento(db: Session, ano: int, subopcao: Contantes.SubOpcoesProc):
    return db.query(models.Processamento).filter(models.Processamento.ano == ano and models.Processamento.subopcao == subopcao.value)

def get_processamento_all(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Processamento).offset(skip).limit(limit).all()

def create_processamento(db: Session, processamento: schemas.Processamento):
    db_processamento = models.Processamento(ano = processamento.ano, 
                                            subopcao = processamento.subopcao,
                                            categoria = processamento.categoria,
                                            produto = processamento.produto,
                                            quantidade = processamento.quantidade)
    db.delete(db_processamento)
    db.add(db_processamento)
    db.commit()
    db.refresh(db_processamento)
    return db_processamento  

#Comercializacao
def get_comercializacao(db: Session, ano: int):
    return db.query(models.Comercializacao).filter(models.Comercializacao.ano == ano)

def get_comercializacao_all(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Comercializacao).offset(skip).limit(limit).all()

def create_comercializacao(db: Session, comercializacao: schemas.Comercializacao):
    db_comercializacao = models.Comercializacao(ano = comercializacao.ano,
                                                categoria = comercializacao.categoria, 
                                                produto = comercializacao.produto, 
                                                quantidade = comercializacao.quantidade)
    db.delete(db_comercializacao)
    db.add(db_comercializacao)
    db.commit()
    db.refresh(db_comercializacao)
    return db_comercializacao

#Importacao
def get_importacao(db: Session, ano: int, subopcao: Contantes.SubOpcoesImport):
    return db.query(models.Importacao).filter(models.Importacao.ano == ano and models.Importacao.subopcao == subopcao.value)

def get_importacao_all(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Importacao).offset(skip).limit(limit).all()

def create_importacao(db: Session, importacao: schemas.Importacao):
    db_importacao = models.Importacao(ano = importacao.ano, 
                                      subopcao = importacao.subopcao,
                                      categoria = importacao.categoria,
                                      produto = importacao.produto,
                                      quantidade = importacao.quantidade)
    db.delete(db_importacao)
    db.add(db_importacao)
    db.commit()
    db.refresh(db_importacao)
    return db_importacao

#Exportacao
def get_exportacao(db: Session, ano: int, subopcao: Contantes.SubOpcoesExport):
    return db.query(models.Exportacao).filter(models.Exportacao.ano == ano and models.Exportacao.subopcao == subopcao.value)

def get_exportacao_all(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Importacao).offset(skip).limit(limit).all()

def create_exportacao(db: Session, exportacao: schemas.Exportacao):
    db_exportacao = models.Importacao(ano = exportacao.ano, 
                                      subopcao = exportacao.subopcao,
                                      categoria = exportacao.categoria,
                                      produto = exportacao.produto,
                                      quantidade = exportacao.quantidade)
    db.delete(db_exportacao)
    db.add(db_exportacao)
    db.commit()
    db.refresh(db_exportacao)
    return db_exportacao