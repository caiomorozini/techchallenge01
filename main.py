from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from Util.Contantes import *
from Util.RestAPI import *
from sqlalchemy.orm import Session
from sql import crud, models, schemas
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech Challenge",)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
async def docs_redirect():
    """
    Redireciona para a documentação Swagger.
    """
    return RedirectResponse(url="/docs")

@app.get("/Producao", tags=["Embrapa"])
async def getProducao(ano: int | None = None, db: Session = Depends(get_db)):
    """
    Obtém dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.

    Parâmetros de Query:
    - ano (opcional): Filtra os dados pelo ano fornecido.

    Retorno:
    - Dados da produção para o ano especificado ou os dados do ano mais recente se não for fornecido.
    """
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    url = base_url + f"?{parametros}opcao={Opcoes.Producao.value}"

    produtos = ExecutarGet(url, ano, "", Opcoes.Producao, db)
    return(produtos)

@app.get("/Processamento", tags=["Embrapa"])
async def getProcessamento(ano: int | None = None, subopcao: SubOpcoesProc | None = None, db: Session = Depends(get_db)):
    """
    Obtém dados de quantidade de uvas processadas no Rio Grande do Sul.

    Parâmetros de Query:
    - ano (opcional): Filtra os dados pelo ano fornecido.
    - subopcao (opcional): Filtra os dados pela subopção de processamento fornecida.

    Retorno:
    - Dados do processamento para o ano e subopção especificados ou os dados do primeira ano e subopção disponíveis se não forem fornecidos.
    """
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoProcessamento(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Processamento.value}"

    produtos = ExecutarGet(url, ano, subopcaovalor, Opcoes.Processamento, db)

    return(produtos)

@app.get("/Comercializacao", tags=["Embrapa"])
async def getComercializacao(ano: int | None = None, db: Session = Depends(get_db)):
    """
    Obtém dados de comercialização de vinhos e derivados no Rio Grande do Sul.

    Parâmetros de Query:
    - ano (opcional): Filtra os dados pelo ano fornecido.

    Retorno:
    - Dados da comercialização para o ano especificado ou os dados do ano mais recente se não for fornecido.
    """
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    url = base_url + f"?{parametros}opcao={Opcoes.Comercializacao.value}"

    produtos = ExecutarGet(url, ano, "", Opcoes.Comercializacao, db)

    return(produtos)

@app.get("/Importacao", tags=["Embrapa"])
async def getImportacao(ano: int | None = None, subopcao: SubOpcoesImport | None = None, db: Session = Depends(get_db)):
    """
    Obtém dados de importação de derivados de uva.

    Parâmetros de Query:
    - ano (opcional): Filtra os dados pelo ano fornecido.
    - subopcao (opcional): Filtra os dados pela subopção de importação fornecida.

    Retorno:
    - Dados da importação para o ano e subopção especificados ou os dados do primeira ano e subopção disponíveis se não forem fornecidos.
    """
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoImportacao(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Importacao.value}"

    produtos = ExecutarGet(url, ano, subopcaovalor, Opcoes.Importacao, db)

    return(produtos)

@app.get("/Exportacao", tags=["Embrapa"])
async def getExportacao(ano: int | None = None, subopcao: SubOpcoesExport | None = None, db: Session = Depends(get_db)):
    """
    Obtém dados de exportação de derivados de uva.

    Parâmetros de Query:
    - ano (opcional): Filtra os dados pelo ano fornecido.
    - subopcao (opcional): Filtra os dados pela subopção de exportação fornecida.

    Retorno:
    - Dados da exportação para o ano e subopção especificados ou os dados do primeira ano e subopção disponíveis se não forem fornecidos.
    """
    parametros = ""
    if ano:
        parametros = f"ano={ano}&"
    if subopcao:
        subopcaovalor = ConsultarSubOpcaoExportacao(subopcao)
        if subopcaovalor:
            parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Exportacao.value}"

    produtos = ExecutarGet(url, ano, subopcaovalor, Opcoes.Exportacao, db)

    return(produtos)
