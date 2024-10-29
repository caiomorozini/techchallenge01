# techchallenge01
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Tech Challenge API</title>
</head>
<body>
    <h1>Tech Challenge API</h1>
    <p>Esta é uma API construída com FastAPI para obter dados de produção, processamento, comercialização, importação e exportação de uvas no Rio Grande do Sul, além de gerenciar usuários.</p>

    <h2>Instalação</h2>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://seu-repositorio.git
cd seu-repositorio</code></pre>
        </li>
        <li>Crie e ative um ambiente virtual:
            <pre><code>python -m venv venv
source venv/bin/activate   # No Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li>Instale as dependências:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Configure a string de conexão no arquivo <code>connection_string.py</code> com as credenciais do Azure SQL Server.</li>
    </ol>

    <h2>Uso</h2>
    <ol>
        <li>Inicie a aplicação:
            <pre><code>uvicorn main:app --reload</code></pre>
        </li>
        <li>Acesse a documentação interativa do Swagger em: <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a></li>
    </ol>

    <h2>Endpoints</h2>
    <h3>Embrapa</h3>
    <ul>
        <li><strong>GET /</strong>: Redireciona para a documentação Swagger.</li>
        <li><strong>GET /Embrapa/Producao</strong>: Obtém dados de produção de vinhos, sucos e derivados do Rio Grande do Sul.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>ano</code> (opcional): Filtra os dados pelo ano fornecido.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>GET /Embrapa/Processamento</strong>: Obtém dados de quantidade de uvas processadas no Rio Grande do Sul.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>ano</code> (opcional): Filtra os dados pelo ano fornecido.</li>
                        <li><code>subopcao</code> (opcional): Filtra os dados pela subopção de processamento fornecida.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>GET /Embrapa/Comercializacao</strong>: Obtém dados de comercialização de vinhos e derivados no Rio Grande do Sul.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>ano</code> (opcional): Filtra os dados pelo ano fornecido.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>GET /Embrapa/Importacao</strong>: Obtém dados de importação de derivados de uva.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>ano</code> (opcional): Filtra os dados pelo ano fornecido.</li>
                        <li><code>subopcao</code> (opcional): Filtra os dados pela subopção de importação fornecida.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>GET /Embrapa/Exportacao</strong>: Obtém dados de exportação de derivados de uva.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>ano</code> (opcional): Filtra os dados pelo ano fornecido.</li>
                        <li><code>subopcao</code> (opcional): Filtra os dados pela subopção de exportação fornecida.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

    <h3>Usuário</h3>
    <ul>
        <li><strong>POST /users/</strong>: Cria um novo usuário.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>user</code>: Esquema do usuário que será criado.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>DELETE /users/{user_id}</strong>: Exclui um usuário existente.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>user_id</code>: ID do usuário a ser excluído.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>POST /token</strong>: Faz login e retorna um token de acesso.
            <ul>
                <li>Parâmetros:
                    <ul>
                        <li><code>form_data</code>: Dados do formulário de login.</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

    <h2>Autenticação</h2>
    <p>A API usa OAuth2 com senha (Bearer Token). Certifique-se de incluir o token de acesso nos cabeçalhos das solicitações protegidas.</p>
</body>
</html>