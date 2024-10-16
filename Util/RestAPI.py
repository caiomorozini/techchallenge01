
import requests
from fastapi import HTTPException
from Util.Contantes import *
import Util.WebScraping as WebScraping
from sql import crud

def ExecutarGet(url:str, ano:int, subopcao:str, opcoes:Opcoes, db: requests.Session):
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

    return(produtos)

def ConsultarSubOpcaoProcessamento(subopcao):
    if subopcao is SubOpcoesProc.Viniferas:
        return("subopt_01")
    elif subopcao is SubOpcoesProc.AmericanasHibridas:
        return("subopt_02")
    elif subopcao is SubOpcoesProc.UvasMesa:
        return("subopt_03")
    elif subopcao is SubOpcoesProc.SemClassificacao:
        return("subopt_04")
    else:
        return("")
    
def ConsultarSubOpcaoImportacao(subopcao):
    if subopcao is SubOpcoesImport.VinhosMesa:
        return("subopt_01")
    elif subopcao is SubOpcoesImport.Espumantes:
        return("subopt_02")
    elif subopcao is SubOpcoesImport.UvasFrescas:
        return("subopt_03")
    elif subopcao is SubOpcoesImport.UvasPassas:
        return("subopt_04")
    elif subopcao is SubOpcoesImport.SucoUva:
        return("subopt_05")
    else:
        return("")
    
def ConsultarSubOpcaoExportacao(subopcao):
    if subopcao is SubOpcoesExport.VinhosMesa:
        return("subopt_01")
    elif subopcao is SubOpcoesExport.Espumantes:
        return("subopt_02")
    elif subopcao is SubOpcoesExport.UvasFrescas:
        return("subopt_03")
    elif subopcao is SubOpcoesExport.SucoUva:
        return("subopt_04")
    else:
        return("")