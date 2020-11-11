import pandas as pd
import os
import collections
import zipfile


class CSVFileReader:

    def __init__(self, filename, ultimo_registro):
        self.filepath = os.path.join(os.getcwd().split(
            "DataExtraction")[0], "DataFiles", filename)
        with zipfile.ZipFile(self.filepath, "r") as zfile:
            zfile.extractall(os.path.join(os.getcwd().split(
                "DataExtraction")[0], "DataFiles"))
        self.filepath = self.filepath.split(".zip")[0] + ".csv"
        self.df = pd.read_csv(self.filepath, usecols=[
                              'estado', 'municipio', 'data', 'casosAcumulado', 'casosNovos', 'obitosAcumulado'], sep=';')
        self.ultimo_registro = ultimo_registro

    def retornar_estados(self):
        return [item for item, count in collections.Counter(self.df["estado"]).items() if count > 1 and item.__class__.__name__ == "str"]

    def retornar_dados(self, estado, colunas):
        aux_df = self.df.loc[(self.df["estado"] == estado) & (
            self.df["data"] == self.ultimo_registro) & (self.df["municipio"].notnull())]
        contadores = []
        for i in range(len(colunas)):
            contadores.append(0)
        for index, dados in aux_df.iterrows():
            for i in range(len(colunas)):
                numero = dados[colunas[i]]
                if numero > 0:
                    contadores[i] += numero
        return contadores

    def retornar_dados_covid(self):
        dados = dict()
        for estado in self.retornar_estados():
            dadosCsv = self.retornar_dados(
                estado, ["casosAcumulado", "obitosAcumulado", "casosNovos"])
            dados[estado] = {
                "casosAcumulados": dadosCsv[0],
                "obitosAcumulados": dadosCsv[1],
                "casosNovos": dadosCsv[2]
            }
        return dados


if __name__ == "__main__":
    csv = CSVFileReader("HIST_PAINEL_COVIDBR_04nov2020.zip", "2020-11-04")
    dados = csv.retornar_dados("RJ", ["casosNovos"])
    os.remove(os.path.join(os.getcwd().split(
        "DataExtraction")[0], "DataFiles", "HIST_PAINEL_COVIDBR_04nov2020.csv"))
