from DataExtraction.CSVFileReader import CSVFileReader
from DataComparation.CovidRank import CovidRank
from SortingAlgorithm.ShellSort import Shell
import os

def formater(x, pos):
    return '{:1.0f}'.format(x*1)

def MedianaCasosNovos(filename, ultima_atualizacao):
    d = CSVFileReader(filename+".zip", ultima_atualizacao)
    c = CovidRank(Shell.decrescent_shell, d.retornar_dados_covid())
    rankCasosNovos = c.retornar_casosNovos_ordem_decrescente()
    labels = []
    dados = []
    for i in rankCasosNovos:
        labels.append(i[0])
        dados.append(i[1])
    dados_crescente = dados[::-1]
    dados_size = len(dados_crescente)
    if dados_size % 2 == 0:
        mediana = (dados_crescente[dados_size-1]+dados_crescente[dados_size])/2
    else:
        mediana = dados_crescente[dados_size//2]
    acima_da_mediana = []
    abaixo_da_mediana = []
    for i, j in zip(labels, dados):
        if j <= mediana:
            abaixo_da_mediana.append([i, j])
        else:
            acima_da_mediana.append([i, j])
    print("ok")
    c.plot_data(
        [x[0] for x in abaixo_da_mediana],
        [x[1] for x in abaixo_da_mediana],
        f"Estados brasileiros abaixo da mediana({ultima_atualizacao}): {mediana}",
        f"Casos novos de {ultima_atualizacao}",
        "casosNovosAbaixoDaMediana",
        formater
    )
    c.plot_data(
        [x[0] for x in acima_da_mediana],
        [x[1] for x in acima_da_mediana],
        f"Estados brasileiros acima da mediana({ultima_atualizacao}): {mediana}",
        f"Casos novos de {ultima_atualizacao}",
        "casosNovosAcimaDaMediana",
        formater
    )
    os.remove(os.path.join(os.getcwd().split(
        "DataExtraction")[0], "DataFiles", filename+".csv"))
