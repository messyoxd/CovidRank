from DataExtraction.CSVFileReader import CSVFileReader
from DataComparation.CovidRank import CovidRank
from SortingAlgorithm.ShellSort import Shell
from rank_casos import RankCasos
from novos_casos_mediana import MedianaCasosNovos
import os

if __name__ == "__main__":
    options = {
        1: "Rank Covid",
        2: "Mediana novos casos"
    }
    option = 2
    filename = "HIST_PAINEL_COVIDBR_04nov2020"
    ultima_atualizacao = "2020-11-04"
    if option == 1:
        print(options[option])
        RankCasos(filename, ultima_atualizacao)
    elif option == 2:
        print(options[option])
        MedianaCasosNovos(filename, ultima_atualizacao)
    else:
        print("Opção invalida!")
