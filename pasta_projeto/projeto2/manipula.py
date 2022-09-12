#Módulo manipula_xls
#Descrição: Este módulo oferece funções para manipular arquivos
#no formato xls.
#Autor: Andrey Azambuja
#Versão: 0.0.1
#Data: hoje

#importação de pacotes
from openpyxl import Workbook

def cria_xls() -> Workbook:
    """Esta função cria uma pasta de trabalho ms-excel"""
    pasta = Workbook()
    return pasta

def cria_planilha(nome_planilha: str, pasta: Workbook) -> None:
    pasta.active
    pasta.create_sheet(nome_planilha)