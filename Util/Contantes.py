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