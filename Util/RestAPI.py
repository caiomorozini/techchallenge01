
import requests
from fastapi import HTTPException
from Util.Contantes import *
import Util.WebScraping as WebScraping

def ExecutarGet(url, Opcoes:Opcoes):
    try:
        page = requests.get(url)
    except Exception as e:
        raise HTTPException(500, "Ocorreu um erro ao tentar efetuar a conexão com o site http://vitibrasil.cnpuv.embrapa.br, tente novamente em alguns minutos")
    try:
        produtos = WebScraping.ExtrairDados(page, Opcoes)
    except Exception as e:
          raise HTTPException(500, f"Erro ao extrair dados da página, {e}")

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