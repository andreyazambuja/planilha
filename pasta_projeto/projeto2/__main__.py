# Importação de pacotes 
## Primeiro importe o que vier da biblioteca padrão
import random

##Depois importe o que vier de pacotes de terceiros
from openpyxl import Workbook


# Importação de pacotes

import manipula

def main():
    lista_planilhas = ['receitas', 'despesas', 'resultados']    
    pasta = manipula.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipula.cria_planilha(planilha, pasta)
    pasta.save("orcamento.xls")


if __name__ == "__main__":
    main()
