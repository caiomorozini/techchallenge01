from http import HTTPStatus
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from Util.Contantes import *
from Util.RestAPI import *
from sqlalchemy.orm import Session
from Util.Security import create_access_token, verify_password, oauth2_scheme
from sql import models, schemas
from sql.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech Challenge",)

@app.get("/", include_in_schema=False)
async def docs_redirect():
    """
    Redireciona para a documentação Swagger.
    """
    return RedirectResponse(url="/docs")

@app.get("/Embrapa/Producao", tags=["Embrapa"])
async def getProducao(ano: int | None = None, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
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

    produtos = ConsultarDadosEmbrapa(url, ano, "", Opcoes.Producao, db)
    return(produtos)

@app.get("/Embrapa/Processamento", tags=["Embrapa"])
async def getProcessamento(ano: int | None = None, subopcao: SubOpcoesProc | None = None, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
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
    else:
        subopcaovalor = "subopt_01"

    if subopcaovalor:
        parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Processamento.value}"

    produtos = ConsultarDadosEmbrapa(url, ano, subopcaovalor, Opcoes.Processamento, db)

    return(produtos)

@app.get("/Embrapa/Comercializacao", tags=["Embrapa"])
async def getComercializacao(ano: int | None = None, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
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

    produtos = ConsultarDadosEmbrapa(url, ano, "", Opcoes.Comercializacao, db)

    return(produtos)

@app.get("/Embrapa/Importacao", tags=["Embrapa"])
async def getImportacao(ano: int | None = None, subopcao: SubOpcoesImport | None = None, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
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
    else:
        subopcaovalor = "subopt_01"

    if subopcaovalor:
        parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Importacao.value}"

    produtos = ConsultarDadosEmbrapa(url, ano, subopcaovalor, Opcoes.Importacao, db)

    return(produtos)

@app.get("/Embrapa/Exportacao", tags=["Embrapa"])
async def getExportacao(ano: int | None = None, subopcao: SubOpcoesExport | None = None, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
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
    else:
        subopcaovalor = "subopt_01"
        
    if subopcaovalor:
        parametros = f"{parametros}subopcao={subopcaovalor}&"

    url = base_url + f"?{parametros}opcao={Opcoes.Exportacao.value}"

    produtos = ConsultarDadosEmbrapa(url, ano, subopcaovalor, Opcoes.Exportacao, db)

    return(produtos)


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=schemas.UserPublic, tags=["Usuario"])
async def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    """
    Cria um novo usuário.

    - **user**: Esquema do usuário que será criado.

    Retorna o usuário criado.
    """
    usuario = CriarUsuario(user, db)
    return usuario

@app.delete('/users/{user_id}', tags=["Usuario"])
async def delete_user(user_id: int, db: Session = Depends(get_db), token = Depends(oauth2_scheme)):
    """
    Exclui um usuário existente.

    - **user_id**: ID do usuário a ser excluído.

    Retorna uma mensagem de sucesso.
    """
    ExcluirUsuario(user_id, db)
    
    return {'message': 'Usuário deletado'}

@app.post('/token', response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Faz login e retorna um token de acesso.

    - **form_data**: Dados do formulário de login.

    Retorna o token de acesso.
    """
    user = ConsultarDadosUsuario_Email(form_data.username, db)

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Usuário ou email inválidos',
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Usuário ou email inválidos',
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}