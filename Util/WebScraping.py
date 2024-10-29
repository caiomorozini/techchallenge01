from Util.Contantes import *
from bs4 import BeautifulSoup as bs
import re
from sql import crud, models


def ExtrairDados(page, opcao:Opcoes):
    produtos = []
    tipo = None
    subopcao = None

    # Parsing do HTML com BeautifulSoup
    soup = bs(page.content, "html.parser")

    #Encontrando o botão de subopção ativo
    subopcao = ConsultarBotaoAtivo(soup, page.content)

    #Encontrando o ano
    ano = ConsultarAno(soup)

    if opcao is Opcoes.Producao or opcao is Opcoes.Processamento or opcao is Opcoes.Comercializacao:
        produtos = ConsultarTabelaProdutos(soup, ano, subopcao, opcao)
    elif opcao is Opcoes.Importacao or opcao is Opcoes.Exportacao:
        produtos = ConsultarTabelaPaises(soup, ano, subopcao, opcao)

    return produtos

def ConsultarBotaoAtivo(soup, html_doc):
    button_value = None
    btn_active = None
    conteudo_botao = ""

    # Converte os dados para string
    html_str = html_doc.decode("utf-8")

    # Identifica o grupo dos botões
    group_button = re.search(r"var btn1 = '(.*?)';", html_str)

    # Identificando o valor do botão a ser ativado
    if group_button:
        button_value = re.search(r"var btn1 = '(.*?)';", html_str).group(1)

        # Encontrando o botão correspondente
        if button_value:
            btn_active = soup.find("button", {"value": button_value})

            # Extraindo o conteúdo do botão
            if btn_active:
                conteudo_botao = btn_active.text
    return conteudo_botao

def ConsultarAno(soup):
    try:
        # Encontrando o div com a classe "content_center"
        content_center_div = soup.find("div", class_="content_center")

        # Encontrando o elemento <p> dentro do div
        p_element = content_center_div.find("p", class_="text_center")

        # Extraindo o texto do elemento <p>
        text = p_element.get_text()

        # Extraindo o ano do texto
        ano = re.search(r"\[(\d{4})\]", text).group(1)

        ano_int = int(ano)
        return(ano_int)
    except:
        return 0

def ConsultarTabelaProdutos(soup, ano, subopcao, opcao):
    produtos = []
    ant_tb_item = False
    table = soup.find("table", class_="tb_dados")

    # table --> tbody --> tr --> td
    for tr in table.find("tbody").select("tr"):
        row = [td for td in tr.select("td")]
        if len(row) == 0:
            continue
        if "tb_item" in row[0]["class"]:
            if ant_tb_item:
                if opcao is Opcoes.Producao:
                    produtos.append(models.Producao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))
                elif opcao is Opcoes.Processamento:            
                    produtos.append(models.Processamento(ano=ano, subopcao=subopcao, categoria=item, produto=subitem, quantidade=quantidade))
                elif opcao is Opcoes.Comercializacao:                     
                    produtos.append(models.Comercializacao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))
            item = row[0].contents[0].strip()
            subitem = ""
            if row[1].contents[0].strip().replace(".", "") == "-" or row[1].contents[0].strip().replace(".", "") == "*" or row[1].contents[0].strip().replace(".", "") == "nd":
                quantidade = 0
            else:
                quantidade = int(row[1].contents[0].strip().replace(".", ""))
            ant_tb_item = True
            continue
        elif "tb_subitem" in row[0]["class"]:
            ant_tb_item = False
            subitem = row[0].contents[0].strip()
            if row[1].contents[0].strip().replace(".", "") == "-" or row[1].contents[0].strip().replace(".", "") == "*" or row[1].contents[0].strip().replace(".", "") == "nd":
                quantidade = 0
            else:
                quantidade = int(row[1].contents[0].strip().replace(".", ""))

        if opcao is Opcoes.Producao:
            produtos.append(models.Producao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))
        elif opcao is Opcoes.Processamento:            
            produtos.append(models.Processamento(ano=ano, subopcao=subopcao, categoria=item, produto=subitem, quantidade=quantidade))
        elif opcao is Opcoes.Comercializacao:                     
            produtos.append(models.Comercializacao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))

    if ant_tb_item:
        if opcao is Opcoes.Producao:
            produtos.append(models.Producao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))
        elif opcao is Opcoes.Processamento:            
            produtos.append(models.Processamento(ano=ano, subopcao=subopcao, categoria=item, produto=subitem, quantidade=quantidade))
        elif opcao is Opcoes.Comercializacao:                     
            produtos.append(models.Comercializacao(ano=ano, categoria=item, produto=subitem, quantidade=quantidade))
    return produtos

def ConsultarTabelaPaises(soup, ano, subopcao, opcao):
    produtos = []
    table = soup.find("table", class_="tb_dados")

    # table --> tbody --> tr --> td
    for tr in table.find("tbody").select("tr"):
        row = [td for td in tr.select("td")]
        if len(row) == 0:
            continue
        pais = row[0].contents[0].strip()
        if row[1].contents[0].strip().replace(".", "") == "-":
            quantidade = 0
        else:
            quantidade = int(row[1].contents[0].strip().replace(".", ""))
        if row[2].contents[0].strip().replace(".", "") == "-":
            valor = 0
        else:
            valor = int(row[2].contents[0].strip().replace(".", ""))

        if opcao is Opcoes.Importacao:
            produtos.append(models.Importacao(ano=ano, subopcao=subopcao, pais=pais, quantidade=quantidade, valor=valor))
        elif opcao is Opcoes.Exportacao:            
            produtos.append(models.Exportacao(ano=ano, subopcao=subopcao, pais=pais, quantidade=quantidade, valor=valor))
    return produtos