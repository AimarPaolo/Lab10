import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._stati = DAO.getAllCountry()
        self._idMap = {}
        for f in self._stati:
            self._idMap[f.CCode] = f
        self._dizionario = {}

    def buildGraph(self, year):
        self._grafo.clear()
        countryPeriod = DAO.getAllCountryExisting(year)
        for f in self._stati:
            if f in countryPeriod:
                self._grafo.add_node(f)
        self.addEdge(year)
        return self._grafo

    def addEdge(self, year):
        connessioni = DAO.getAllConfiniPerAnno(year)
        for con in connessioni:
            c1 = self._idMap[con.state1no]
            c2 = self._idMap[con.state2no]
            if self._grafo.has_edge(c1, c2) is False:
                self._grafo.add_edge(c1, c2)

    def getVicini(self, year):
        self._dizionario = {}
        self.addEdge(year)
        for vertice in self._grafo.nodes:
            self._dizionario[vertice] = self._grafo.degree(vertice)
        return self._dizionario

    def numEdges(self):
        return len(self._grafo.edges)

    def numNodes(self):
        return len(self._grafo.nodes)

    def getCountry(self, year):
        return DAO.getAllCountry()

    def getConnessi(self):
        return nx.number_connected_components(self._grafo)

    def getNodiConnessi(self, nodoIniziale):
        nodo = self._idMap[int(nodoIniziale)]
        return nx.dfs_predecessors(self._grafo, nodo)