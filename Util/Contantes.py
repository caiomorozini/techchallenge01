from enum import Enum

base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"

class Opcoes(str, Enum):
    Producao = "opt_02"
    Processamento = "opt_03"
    Comercializacao = "opt_04"
    Importacao = "opt_05"
    Exportacao = "opt_06"

class SubOpcoesProc(str, Enum):
    Viniferas = "Viniferas"
    AmericanasHibridas = "AmericanasHibridas"
    UvasMesa = "UvasMesa"
    SemClassificacao = "SemClassificacao"

class SubOpcoesImport(str, Enum):
    VinhosMesa = "VinhosMesa"
    Espumantes = "Espumantes"
    UvasFrescas = "UvasFrescas"
    UvasPassas = "UvasPassas"
    SucoUva = "SucoUva"

class SubOpcoesExport(str, Enum):
    VinhosMesa = "VinhosMesa"
    Espumantes = "Espumantes"
    UvasFrescas = "UvasFrescas"
    SucoUva = "SucoUva"

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