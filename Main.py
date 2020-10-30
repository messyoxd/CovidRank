from DataExtraction.CSVFileReader import CSVFileReader
from DataComparation.CovidRank import CovidRank
from SortingAlgorithm.ShellSort import Shell
import os
if __name__ == "__main__":
    filename = "HIST_PAINEL_COVIDBR_28out2020"
    d = CSVFileReader(filename+".zip", "2020-10-28")
    c = CovidRank(Shell.decrescent_shell, d.retornar_dados_covid(8))
    rank = c.retornar_casosAcumulados_ordem_decrescente()
    print(rank)

    os.remove(os.path.join(os.getcwd().split(
        "DataExtraction")[0], "DataFiles", filename+".csv"))
