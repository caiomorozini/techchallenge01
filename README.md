# Tech Challenge API

Esta é uma API construída com FastAPI para obter dados de produção, processamento, comercialização, importação e exportação de uvas no Rio Grande do Sul, além de gerenciar usuários.

## Aplicação publicada

A Aplicação foi publicada no Azure, é possível acessa-la em: [https://techchallengeembrapa.azurewebsites.net/]

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/caiomorozini/techchallenge01
    cd seu-repositorio
    ```
2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Crie o arquivo `connection_string.py` na pasta sql, o seu conteúdo se encontra dentro do word anexado no tech challenge.

## Uso

1. Inicie a aplicação:
    ```sh
    uvicorn main:app --reload
    ```
2. Acesse a documentação interativa do Swagger em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints

### Embrapa

- **GET /**: Redireciona para a documentação Swagger.
- **GET /Embrapa/Producao**: Obtém dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.
  - Parâmetros:
    - `ano` : Filtra os dados pelo ano fornecido.
- **GET /Embrapa/Processamento**: Obtém dados de quantidade de uvas processadas no Rio Grande do Sul.
  - Parâmetros:
    - `ano` : Filtra os dados pelo ano fornecido.
    - `subopcao` : Filtra os dados pela subopção de processamento fornecida.
- **GET /Embrapa/Comercializacao**: Obtém dados de comercialização de vinhos e derivados no Rio Grande do Sul.
  - Parâmetros:
    - `ano` : Filtra os dados pelo ano fornecido.
- **GET /Embrapa/Importacao**: Obtém dados de importação de derivados de uva.
  - Parâmetros:
    - `ano` : Filtra os dados pelo ano fornecido.
    - `subopcao` : Filtra os dados pela subopção de importação fornecida.
- **GET /Embrapa/Exportacao**: Obtém dados de exportação de derivados de uva.
  - Parâmetros:
    - `ano` : Filtra os dados pelo ano fornecido.
    - `subopcao` : Filtra os dados pela subopção de exportação fornecida.

### Usuário

- **POST /users/**: Cria um novo usuário.
  - Parâmetros:
    - `user`: Esquema do usuário que será criado.
- **DELETE /users/{user_id}**: Exclui um usuário existente.
  - Parâmetros:
    - `user_id`: ID do usuário a ser excluído.
- **POST /token**: Faz login e retorna um token de acesso.
  - Parâmetros:
    - `form_data`: Dados do formulário de login.

## Autenticação

A API usa OAuth2 com senha (Bearer Token). Certifique-se de incluir o token de acesso nos cabeçalhos das solicitações protegidas.