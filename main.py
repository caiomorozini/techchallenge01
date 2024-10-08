from fastapi import FastAPI
import requests
from Classes.Enums import Opcoes
from Classes.Enums import SubOpcoesProc
from Classes.Enums import SubOpcoesImport
from Classes.Enums import SubOpcoesExport
import Util.WebScraping as WebScraping

api_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"
app = FastAPI()

##TODO LIST
##FAZER O SWAGGER
##VERIFICAR SE EXISTE UMA FORMA MELHOR DE RECEBER A DESCRIÇÃO PELO LINK E UTILIZAR O VALOR
##DATACLASSES PYDANTIC RENDER
##GRAVAR EM UM HTML PARA CONSULTA CASO ESTEJA OFFLINE


@app.get("/Producao")
async def getProducao(ano:int | None = None):
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    url = api_url + f"?{parametros}opcao={Opcoes.Producao.value}"

    #Precisa colocar o error handling
    page = requests.get(url)

    produtos = WebScraping.ExtrairDados(page)

    return(produtos)

@app.get("/Processamento")
async def getProcessamento(ano:int | None = None, subopcao:SubOpcoesProc | None = None):
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoProcessamento(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = api_url + f"?{parametros}opcao={Opcoes.Processamento.value}"

    #Precisa colocar o error handling
    page = requests.get(url)
    
    produtos = WebScraping.ExtrairDados(page)

    return(produtos)

@app.get("/Comercializacao")
async def getComercializacao(ano:int | None = None):
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    url = api_url + f"?{parametros}opcao={Opcoes.Comercializacao.value}"

    #Precisa colocar o error handling
    page = requests.get(url)
    
    produtos = WebScraping.ExtrairDados(page)

    return(produtos)

@app.get("/Importacao")
async def getImportacao(ano:int | None = None, subopcao:SubOpcoesImport | None = None):
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoImportacao(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = api_url + f"?{parametros}opcao={Opcoes.Importacao.value}"

    #Precisa colocar o error handling
    page = requests.get(url)
    
    produtos = WebScraping.ExtrairDadosImport(page)

    return(produtos)

@app.get("/Exportacao")
async def getExportacao(ano:int | None = None, subopcao:SubOpcoesExport | None = None):
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoExportacao(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = api_url + f"?{parametros}opcao={Opcoes.Exportacao.value}"

    #Precisa colocar o error handling
    page = requests.get(url)
    
    produtos = WebScraping.ExtrairDadosImport(page)

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