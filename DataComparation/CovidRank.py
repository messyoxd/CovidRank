
class CovidRank:

    def __init__(self, sort_algorithm, data):
        self.sort_algorithm = sort_algorithm
        self.data = data

    def retornar_casosAcumulados_ordem_decrescente(self) -> list:
        estado_casos = list()        
        for key in self.data.keys():
            estado_casos.append((key, self.data[key]["casosAcumulados"].result()))
        print(estado_casos)
        return self.sort_algorithm(estado_casos, len(estado_casos))