from enum import Enum

base_url = "http://vitibrasil.cnpuv.embrapa.br/index.php"

class Opcoes(str, Enum):
    Producao = "opt_02"
    Processamento = "opt_03"
    Comercializacao = "opt_04"
    Importacao = "opt_05"
    Exportacao = "opt_06"

class SubOpcoesProc(str, Enum):
    Viniferas = "Viníferas"
    AmericanasHibridas = "Americanas e híbridas"
    UvasMesa = "Uvas de mesa"
    SemClassificacao = "Sem classificação"

class SubOpcoesImport(str, Enum):
    VinhosMesa = "Vinhos de mesa"
    Espumantes = "Espumantes"
    UvasFrescas = "Uvas frescas"
    UvasPassas = "Uvas passas"
    SucoUva = "Suco de uva"

class SubOpcoesExport(str, Enum):
    VinhosMesa = "Vinhos de mesa"
    Espumantes = "Espumantes"
    UvasFrescas = "Uvas frescas"
    SucoUva = "Suco de uva"