import random

class RandomWalker:
    def __init__(self, g):
        self.g = g

    def get_nodo_inicial(self):
        nodes = list(self.g.nodes())
        nodo_actual = random.choice(nodes)
        return nodo_actual

    def get_nodo_teletrans(self):
        nodes = list(self.g.nodes())
        nodo_actual = random.choice(nodes)
        return nodo_actual

    def get_nodo_vecinos(self, nodo):
        neigh = list(self.g.out_edges(nodo))
        caminos = []
        if len(neigh) != 0:
            for x in neigh:
                caminos.append(x[1])
            nodo_actual = random.choice(caminos)
            return nodo_actual
        else:
            return nodo

    def get_caminos(self, nodo):
        neigh = list(self.g.out_edges(nodo))
        caminos = []
        if len(neigh) != 0:
            for x in neigh:
                caminos.append(x[1])
        return caminos





