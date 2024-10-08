from Classes.Produto import Produto, ProdutoImport
from bs4 import BeautifulSoup as bs
import re

def ExtrairDados(page):
    produtos = []
    tipo = None
    subopcao = None
    soup = bs(page.content, "html.parser")

    #Encontrando o botão de subopção ativo
    button = table = soup.find_all("button", {"id":"btn1_active"})
    if button:
        subopcao = button.get_text()

    # Encontrando o div com a classe 'content_center'
    content_center_div = soup.find('div', class_='content_center')

    # Encontrando o elemento <p> dentro do div
    p_element = content_center_div.find('p', class_='text_center')

    # Extraindo o texto do elemento <p>
    text = p_element.get_text()

    # Extraindo o ano do texto
    ano = re.search(r'\[(\d{4})\]', text).group(1)

    table = soup.find('table', class_='tb_dados')

    # table --> tbody --> tr --> td
    for tr in table.find('tbody').select('tr'):
        row = [td for td in tr.select('td')]
        if len(row) == 0:
            continue
        if 'tb_item' in row[0]['class']:
            tipo = row[0].contents[0].strip()
            continue
        if 'tb_subitem' in row[0]['class']:
            produto = row[0].contents[0].strip()
            if row[1].contents[0].strip().replace('.', '') == "-":
                quantidade = 0
            else:
                quantidade = int(row[1].contents[0].strip().replace('.', ''))
            produtos.append(Produto(ano, subopcao, tipo, produto, quantidade))

    return produtos

def ExtrairDadosImport(page):
    produtosImport = []
    soup = bs(page.content, "html.parser")

    #Encontrando a subopção
    #subopcao = table = soup.find('button', id='btn1_active').contents[0]
    subopcao = None

    # Encontrando o div com a classe 'content_center'
    content_center_div = soup.find('div', class_='content_center')

    # Encontrando o elemento <p> dentro do div
    p_element = content_center_div.find('p', class_='text_center')

    # Extraindo o texto do elemento <p>
    text = p_element.get_text()

    # Extraindo o ano do texto
    ano = re.search(r'\[(\d{4})\]', text).group(1)

    table = soup.find('table', class_='tb_dados')

    # table --> tbody --> tr --> td
    for tr in table.find('tbody').select('tr'):
        row = [td for td in tr.select('td')]
        if len(row) == 0:
            continue
        pais = row[0].contents[0].strip()
        if row[1].contents[0].strip().replace('.', '') == "-":
            quantidade = 0
        else:
            quantidade = int(row[1].contents[0].strip().replace('.', ''))
        if row[2].contents[0].strip().replace('.', '') == "-":
            valor = 0
        else:
            valor = int(row[1].contents[0].strip().replace('.', ''))
        produtosImport.append(ProdutoImport(ano, subopcao, pais, quantidade, valor))

    return produtosImport