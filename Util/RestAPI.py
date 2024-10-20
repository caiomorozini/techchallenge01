
from http import HTTPStatus
import requests
from fastapi import HTTPException
from Util.Contantes import *
import Util.WebScraping as WebScraping
from sql import crud
from sql.schemas import UserSchema

def ConsultarDadosEmbrapa(url:str, ano:int, subopcao:str, opcoes:Opcoes, db: requests.Session):
    consulta_html = True
    try:
        page = requests.get(url)
        try:
            produtos = WebScraping.ExtrairDados(page, opcoes)  
        except Exception as e:
            raise HTTPException(500, f"Erro ao extrair dados da página, {e}")
    except:
        consulta_html = False
        try:
            if opcoes.value == Opcoes.Producao:
                produtos = crud.get_dados_producao(db, ano)
            elif opcoes.value == Opcoes.Processamento:
                produtos = crud.get_dados_processamento(db, ano, subopcao)
            elif opcoes.value == Opcoes.Comercializacao:
                produtos = crud.get_dados_comercializacao(db, ano)
            elif opcoes.value == Opcoes.Importacao:
                produtos = crud.get_dados_importacao(db, ano, subopcao)
            elif opcoes.value == Opcoes.Exportacao:
                produtos = crud.get_dados_exportacao(db, ano, subopcao)
        except Exception as e:
            raise HTTPException(500, "Ocorreu um erro ao efetuar a conexão com o site http://vitibrasil.cnpuv.embrapa.br, tente novamente em alguns minutos")
        
    if consulta_html:
        try:
            if opcoes.value == Opcoes.Producao:
                crud.insert_dados_producao(db, produtos)
            elif opcoes.value == Opcoes.Processamento:
                crud.insert_dados_processamento(db, produtos)
            elif opcoes.value == Opcoes.Comercializacao:
                crud.insert_dados_comercializacao(db, produtos)
            elif opcoes.value == Opcoes.Importacao:
                crud.insert_dados_importacao(db, produtos)
            elif opcoes.value == Opcoes.Exportacao:
                crud.insert_dados_exportacao(db, produtos)
        except Exception as e:
            raise HTTPException(500, f"Ocorreu um erro ao gravar o histórico da consulta, {e}")

    if produtos:
        return(produtos)
    else:
        raise HTTPException(
                status_code=HTTPStatus.NO_CONTENT,
                detail='Nenhum dado encontrado para a consulta efetuada',
            )

    
def CriarUsuario(user:UserSchema, db: requests.Session):
    db_user = crud.get_dados_usuario(user, db)

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Nome do usuário já está sendo utilizado',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )
    db_user = crud.insert_dados_usuario(user, db)

    return(db_user)

def ExcluirUsuario(user_id:int, db:requests.session):
    db_user = crud.get_dados_usuario_userid(user_id, db)
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado'
        )
    
    crud.delete_dados_usuario(db_user, db)
    return

def ConsultarDadosUsuario_Email(email:str, db:requests.session):
    db_user = crud.get_dados_usuario_email(email, db)
    return(db_user)