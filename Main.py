from DataExtraction.CSVFileReader import CSVFileReader
from DataComparation.CovidRank import CovidRank
from SortingAlgorithm.ShellSort import Shell
import os

def formater(x, pos):
        return '{:1.0f}'.format(x*1)

if __name__ == "__main__":
    filename = "HIST_PAINEL_COVIDBR_28out2020"
    ultima_atualizacao = "2020-10-28"
    d = CSVFileReader(filename+".zip", ultima_atualizacao)
    c = CovidRank(Shell.decrescent_shell, d.retornar_dados_covid(8))
    rankCasosAcumulados = c.retornar_casosAcumulados_ordem_decrescente()
    labels = []
    dados = []
    for i in rankCasosAcumulados:
        labels.append(i[0])
        dados.append(i[1])
    c.plot_data(
        labels,
        dados,
        "Comparacao de casos acumulados dos estados brasileiros",
        f"Casos Acumulados até {ultima_atualizacao}",
        "casosAcumulados",
        formater
    )
    rankObitosAcumulados = c.retornar_obitosAcumulados_ordem_decrescente()
    labels = []
    dados = []
    for i in rankObitosAcumulados:
        labels.append(i[0])
        dados.append(i[1])
    c.plot_data(
        labels,
        dados,
        "Comparacao de óbitos acumulados dos estados brasileiros",
        f"Casos Acumulados até {ultima_atualizacao}",
        "obitosAcumulados",
        formater
    )
    rankCasosNovos = c.retornar_casosNovos_ordem_decrescente()
    labels = []
    dados = []
    for i in rankCasosNovos:
        labels.append(i[0])
        dados.append(i[1])
    c.plot_data(
        labels,
        dados,
        "Comparacao de novos casos dos estados brasileiros",
        f"Casos novos de {ultima_atualizacao}",
        "casosNovos",
        formater
    )
    os.remove(os.path.join(os.getcwd().split(
        "DataExtraction")[0], "DataFiles", filename+".csv"))
