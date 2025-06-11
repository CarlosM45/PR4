# Carlos Alejandro Mercado Villalvazo
# Librería para máximos
import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Función para imprimir el árbol de expansión mínima representado por el array parent
    def printMST(self, parent):
        print("Camino \tPeso")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])

    # Función para encontrar el vértice con mínima distancia que aún no esté incluído en el MST
    def minKey(self, key, mstSet):

        # Inicializar valor mínimo
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Función para construir el árbol de expansión mínima usando el algoritmo de Prim con el grafo representado por la matriz de adyacencia
    def primMST(self):

        # Valores clave para seleccionar el vértice con la distancia mínima (inicialmente infinito)
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Arreglo para almacenar el árbol de expansión mínima
        # Hacer que el primer vértice sea el primero en ser incluido en el MST
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # El primer vértice es la raíz del MST

        for cout in range(self.V):

            # Elegir el vértice con la distancia mínima del conjunto de vértices no incluidos en el MST
            # u siempre es igual a 0 en la primera iteración
            u = self.minKey(key, mstSet)
            print("Vértice seleccionado:", u)

            # Poner el vértice con la distancia mínima en el MST
            mstSet[u] = True
            print("Conjunto de MST actualizado:", mstSet)
            print("Clave actualizada:", key)

            # Actualizar la distancia de los vértices adyacentes sólo si el peso de la arista es menor que la distancia actual
            for v in range(self.V):

                # graph[u][v] no es 0 para aristas adyacentes
                # mstSet[v] es falso para vértices no incluidos en el MST
                # Actualizar la clave sólo si graph[u][v] es menor que key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False \
                and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    print(f"Actualizando clave de {v} a {key[v]} con padre {u}")
            print("Estado de claves después de la iteración:", key)

        self.printMST(parent)


# Código de prueba
if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()
