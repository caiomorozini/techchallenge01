
import requests
from fastapi import HTTPException
from Util.Contantes import *
import Util.WebScraping as WebScraping
from sql import crud

def ExecutarGet(url:str, ano:int, subopcao:str, opcoes:Opcoes, db: requests.Session):
    try:
        page = requests.get(url)
        try:
            produtos = WebScraping.ExtrairDados(page, opcoes)  
        except Exception as e:
            raise HTTPException(500, f"Erro ao extrair dados da página, {e}")
    except:
        try:
            if opcoes.value == Opcoes.Producao:
                produtos = crud.get_producao(db, ano)
            elif opcoes.value == Opcoes.Processamento:
                produtos = crud.get_processamento(db, ano, subopcao)
            elif opcoes.value == Opcoes.Comercializacao:
                produtos = crud.get_comercializacao(db, ano)
            elif opcoes.value == Opcoes.Importacao:
                produtos = crud.get_importacao(db, ano, subopcao)
            elif opcoes.value == Opcoes.Exportacao:
                produtos = crud.get_exportacao(db, ano, subopcao)
        except Exception as e:
            raise HTTPException(500, "Ocorreu um erro ao tentar efetuar a conexão com o site http://vitibrasil.cnpuv.embrapa.br, tente novamente em alguns minutos")
    try:
        if opcoes.value == Opcoes.Producao:
            produto_aux = crud.get_producao(db, ano)
            if not produto_aux: 
                for produto in produtos:
                    crud.create_producao(db, produto)
        elif opcoes.value == Opcoes.Processamento:
            produtos = crud.get_processamento(db, ano, subopcao)
        elif opcoes.value == Opcoes.Comercializacao:
            produtos = crud.get_comercializacao(db, ano)
        elif opcoes.value == Opcoes.Importacao:
            produtos = crud.get_importacao(db, ano, subopcao)
        elif opcoes.value == Opcoes.Exportacao:
            produtos = crud.get_exportacao(db, ano, subopcao)
    except Exception as e:
        raise HTTPException(500, f"Ocorreu um erro ao tentar gravar o histórico da consulta, {e}")

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