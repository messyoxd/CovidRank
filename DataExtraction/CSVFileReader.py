import pandas as pd
import os
import collections
from datetime import date
from concurrent.futures import ProcessPoolExecutor
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

    def retornar_casos_novos_por_estado(self, estado):
        aux_df = self.df.loc[(self.df["estado"] == estado) & (
            self.df["data"] == self.ultimo_registro) & (self.df["municipio"].notnull())]
        casos = 0
        for index, casosNovos in aux_df.iterrows():
            casos += casosNovos["casosNovos"]
        return casos

    def retornar_casos_acumulados_por_estado(self, estado):
        aux_df = self.df.loc[(self.df["estado"] == estado) & (
            self.df["data"] == self.ultimo_registro) & (self.df["municipio"].notnull())]
        casos = 0
        for index, casosAcumulado in aux_df.iterrows():
            casos += casosAcumulado["casosAcumulado"]
        return casos

    def retornar_obitos_acumulados_por_estado(self, estado):
        aux_df = self.df.loc[(self.df["estado"] == estado) & (
            self.df["data"] == self.ultimo_registro) & (self.df["municipio"].notnull())]
        obitos = 0
        for index, obitosAcumulado in aux_df.iterrows():
            obitos += obitosAcumulado["obitosAcumulado"]
        return obitos
    
    def retornar_dados(self, estado, colunas):
      aux_df = self.df.loc[(self.df["estado"] == estado) & (
            self.df["data"] == self.ultimo_registro) & (self.df["municipio"].notnull())]
      contadores = []
      for i in range(len(colunas)):
        contadores.append(0)
      for index, dados in aux_df.iterrows():
        for i in range(len(colunas)):
          contadores[i] += dados[colunas[i]]
      return contadores

    def retornar_dados_covid(self):
        dados = dict()
        for estado in self.retornar_estados():
            dadosCsv = self.retornar_dados(estado, ["casosAcumulado", "obitosAcumulado", "casosNovos"])
            dados[estado] = {
              "casosAcumulados": dadosCsv[0],
              "obitosAcumulados": dadosCsv[1],
              "casosNovos": dadosCsv[2]
            }
            # dados[estado] = {
            #     "casosAcumulados": self.retornar_casos_acumulados_por_estado(estado),
            #     "obitosAcumulados": self.retornar_obitos_acumulados_por_estado(estado),
            #     "casosNovos": self.retornar_casos_novos_por_estado(estado),
            # }
        return dados


if __name__ == "__main__":
    csv = CSVFileReader("HIST_PAINEL_COVIDBR_28out2020.zip", "2020-10-28")
    os.remove(os.path.join(os.getcwd().split(
        "DataExtraction")[0], "DataFiles", "HIST_PAINEL_COVIDBR_28out2020.csv"))
    # dados = csv.retornar_dados_covid(1)
    # b = dados["CE"]["casosAcumulados"].result()
    # print(b)
