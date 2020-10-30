
import matplotlib.pyplot as plt


class CovidRank:

    def __init__(self, sort_algorithm, data):
        self.sort_algorithm = sort_algorithm
        self.data = data

    def retornar_casosNovos_ordem_decrescente(self) -> list:
        estado_casos = list()
        for key in self.data.keys():
            estado_casos.append(
                (key, self.data[key]["casosNovos"].result()))
        return self.sort_algorithm(estado_casos, len(estado_casos))

    def retornar_casosAcumulados_ordem_decrescente(self) -> list:
        estado_casos = list()
        for key in self.data.keys():
            estado_casos.append(
                (key, self.data[key]["casosAcumulados"].result()))
        return self.sort_algorithm(estado_casos, len(estado_casos))

    def retornar_obitosAcumulados_ordem_decrescente(self) -> list:
        estado_obitos = list()
        for key in self.data.keys():
            estado_obitos.append(
                (key, self.data[key]["obitosAcumulados"].result()))
        return self.sort_algorithm(estado_obitos, len(estado_obitos))    

    def plot_data(self, labels, data, title, ylabel, filename, formater) -> None:
        ###### Plotar os dados ###############
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.yaxis.set_major_formatter(formater)
        ax.bar(labels, data)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.bar(labels, data, color="blue")
        fig.savefig(f'{filename}.png')
        ######################################

