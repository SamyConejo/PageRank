import numpy as np
from RandomWalker import RandomWalker
from utils import vector_format


class PowerIterator:

    def __init__(self, m_matrix, r_vector, g, google_matrix):
        self.m_matrix = m_matrix
        self.r_vector = r_vector
        self.g = g
        self.google_matrix = google_matrix
        self.tipo_tramp = ''
        self.initial_vector = self.r_vector
        self.random_walker = RandomWalker(self.g)

    def evaluate_trap(self, nodo):
        tipo_tramp = ''
        caminos = list(self.g.out_edges(nodo))

        # si el nodo tiene solo un enlace posible spider
        if len(caminos) == 1:
            temp_1 = caminos[0][0]
            temp_2 = caminos[0][1]
            # si el enlace es consigo mismo spider
            if temp_1 == temp_2:
                tipo_tramp = 'spider'
        # si el nodo no tiene enlaces
        elif not self.g.out_edges(nodo):
            tipo_tramp = 'deadend'
        else:
            tipo_tramp = 'normal'

        if tipo_tramp == 'spider':
            respuesta = input('Estas atrapado en un spidertrap, hacer teletransportacion? (s/n)\n')
            if respuesta == 'n':
                pass
            elif respuesta == 's':
                self.m_matrix = self.google_matrix
                self.r_vector_ = self.initial_vector
                return 'teletrans'

        elif tipo_tramp == 'deadend':
            respuesta = input('Estas atrapado en un deadend, hacer teletransportacion? (s/n)\n')
            if respuesta == 'n':
                pass
            elif respuesta == 's':
                self.m_matrix = self.google_matrix
                self.r_vector_ = self.initial_vector

                return 'teletrans'

    def print_ranking(self, nodos_visitados, tiempo_t, r_vector, nodo_actual):
        print('Nodo actual', nodos_visitados)
        print('Posibles caminos ',self.random_walker.get_caminos(nodo_actual))
        print('Iteration ', str(tiempo_t), ' \t\tRanking')
        vector_format(r_vector)

    def run(self):
        tiempo_t = 0
        nodos_visitados = []
        set_nodes = set()
        teletrans = False
        temp_vector = self.r_vector

        # tiempo 0
        nodo_actual = self.random_walker.get_nodo_inicial()
        nodos_visitados.append(nodo_actual)
        set_nodes.add(nodo_actual)
        self.print_ranking(nodos_visitados, tiempo_t, temp_vector, nodo_actual)
        tiempo_t += 1


        decision = self.evaluate_trap(nodo_actual)
        while len(set_nodes) < 15:
            if decision == 'teletrans':
                nodo_actual = self.random_walker.get_nodo_teletrans()
                nodos_visitados.append(nodo_actual)
                set_nodes.add(nodo_actual)
                self.print_ranking(nodos_visitados, tiempo_t, self.r_vector, nodo_actual)
                tiempo_t += 1
                decision = 'active'
            else:
                if decision == 'active':
                    nodo_actual = self.random_walker.get_nodo_teletrans()
                else:
                    nodo_actual = self.random_walker.get_nodo_vecinos(nodo_actual)
                temp_vector = np.dot(self.m_matrix, temp_vector)
                nodos_visitados.append(nodo_actual)
                set_nodes.add(nodo_actual)
                self.print_ranking(nodos_visitados, tiempo_t, temp_vector, nodo_actual)
                tiempo_t += 1
                if decision == 'active':
                    pass
                else:
                    decision = self.evaluate_trap(nodo_actual)








