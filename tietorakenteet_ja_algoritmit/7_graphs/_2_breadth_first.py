class Vertex:
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return f'<Vertex: {self._value}>'
    def __hash__(self):
        return hash(id(self))


class Edge:
    def __init__(self, u, v, x):
        self._first = u
        self._second = v
        self._value = x

    def __repr__(self):
        return f'<Edge ({self._value}): {self._first} --> {self._second}>'

    def endpoints(self):
        return (self._first, self._second)

    def opposite(self, v):
        return self._second if v is self._first else self._first

    def value(self):
        return self._value

    def __hash__(self):
        return hash((self._first, self._second))

class Graph:
    def __init__(self, adj_map=None):
        if adj_map:
            self._adj_map = adj_map
        else:
            self._adj_map = {}

    def get_vertices(self):
        return self._adj_map.keys()

    def get_edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        for secondary_map in self._adj_map.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """
        Returns the edge from u to v, or None if not adjacents.
        """
        return self._adj_map[u].get(v)

    def degree(self, u):
        """
        Returns the number of edges incident to vertex u
        """
        return len(self._adj_map[u])

    def get_adjacent_vertices(self, u):
        """
        Return a list of the adjacent vertices of a given vertex
        """
        return list(self._adj_map[u].keys())

    def get_incident_edges(self, u):
        """
        Returns edges incident to vertex u
        """
        return list(self._adj_map[u].values())

    def add_vertex(self, value):
        vertex = Vertex(value)
        self._adj_map[vertex] = {}
        return vertex

    def add_edge(self, u, v, x=None):
        edge = Edge(u, v, x)
        self._adj_map[u][v] = edge
        self._adj_map[v][u] = edge

    def get_adj_map(self):
        return self._adj_map

    def get_adj_matrix(self):
        all_vertices = self._adj_map.keys()

        return [[int(bool(self._adj_map[u].get(v))) for v in all_vertices] for u in
            all_vertices]


def BFS_incorrect(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """

    #search function
    def recursive_wide_search(target_vertex, origin_vertex, graph, dictionary, visited):
        #add root vertex
        if origin_vertex is None:
            dictionary[target_vertex] = origin_vertex

        #visited means search hs been called on a vertex, not if its been added...
        visited.add(target_vertex)

        edges = graph._adj_map[target_vertex]
        #add direct children
        if len(edges) > 0:
            #add all children first
            for child_vertex in edges.keys():
                if child_vertex not in visited:
                    dictionary[child_vertex] = target_vertex

            #then call wide search on direct children
            for child_vertex in edges.keys():
                if child_vertex not in visited:
                    recursive_wide_search(child_vertex, target_vertex, graph, dictionary, visited)

        else:
            pass

    #fill dictionary with search
    visited = set()
    dictionary = {}
    origin = None
    recursive_wide_search(u, origin, graph, dictionary, visited)

    return dictionary


def BFS(graph, u, visited=None):

    #search function
    def wide_search(target_array, graph, dictionary, visited):

        while len(target_array) > 0:
            next_level_array = []

            for target_vertex in target_array:

                visited.add(target_vertex)

                #get adjacents
                #adjacent = graph.get_adjacent_vertices(target_vertex)
                adjacent = graph._adj_map[target_vertex].keys()

                #add all adjacent children
                for vertex in adjacent:
                    if vertex not in visited and vertex not in next_level_array:
                        dictionary[vertex] = target_vertex
                        next_level_array.append(vertex)

            target_array = next_level_array

        return

    #fill dictionary with search
    visited = set()
    dictionary = {u: None}
    level = 0
    wide_search([u], graph, dictionary, visited)

    return dictionary



if __name__ == '__main__':
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    E = Vertex('E')
    F = Vertex('F')

    AB = Edge(A, B, 2)
    AC = Edge(A, C, 4)
    BD = Edge(B, D, 5)
    CD = Edge(C, D, 9)
    CE = Edge(C, E, 3)
    DF = Edge(D, F, 2)
    EF = Edge(E, F, 2)

    adj_map = {
        A: {B: AB, C: AC},
        B: {A: AB, D: BD},
        C: {A: AC, D: CD, E: CE},
        D: {B: BD, C: CD, F: DF},
        E: {C: CE, F: EF},
        F: {D: DF, E: EF}
    }

    g = Graph(adj_map)
    print(BFS(g, A))

    print('''{<Vertex: A>: None, <Vertex: B>: <Vertex: A>, <Vertex: C>: <Vertex: A>, <Vertex: D>: <Vertex: B>, <Vertex: E>: <Vertex: C>, <Vertex: F>: <Vertex: D>}''')


