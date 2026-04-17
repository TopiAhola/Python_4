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




"""As a reminder, the graph object offers some methods that can be used in this case:

get_vertices(): Return a list of vertices on the graph
get_vertices(u): Return a list of the adjacent vertices of a given vertex
get_edges(): Return a set of all edges of the graph.
get_edge(u, v): Returns the edge from u to v, or None if not adjacents.
degree(u): Returns the number of edges incident to vertex u.
get_adjacent_vertices(u): Return a list of the adjacent vertices of a given vertex
get_incident_edges(u): Returns edges incident to vertex u."""



def dijkstra_shortest_path(start, end, graph):
    """The function returns a tuple containing the minimum distance between vertices and a list of vertices that form
    the minimum path from one vertex to the other."""

    #initialize path set
    shortest_path_to = {}
    # list of unvisited veritces
    unvisited_vertices = []

    infinite = float('inf')
    for vertex in graph.get_vertices():
        shortest_path_to[vertex] = {'shortest': infinite, 'previous': None }
        unvisited_vertices.append(vertex)

    #set start to path set
    shortest_path_to[start] = {'shortest': 0, 'previous': None}

    #loop all unvisited vertices
    current_vertex = start
    while unvisited_vertices:

        # get the shortest distance vertex (start at first)
        current_vertex = unvisited_vertices[0]

        for key_vertex, value in shortest_path_to.items():
            if key_vertex in unvisited_vertices and shortest_path_to[current_vertex]['shortest'] > value['shortest']:
                current_vertex = key_vertex

        distance = shortest_path_to[current_vertex]['shortest']

        #get adjacent vertices
        adjacent_vertices = graph.get_adjacent_vertices(current_vertex)
        for vertex in adjacent_vertices:
            if vertex in unvisited_vertices:
                distance_to_start = distance + graph.get_edge(vertex, current_vertex).value()

                #if this path is shorter than the existing one, replace
                if distance_to_start < shortest_path_to[vertex]['shortest']:
                    shortest_path_to[vertex]['previous'] = current_vertex
                    shortest_path_to[vertex]['shortest'] = distance_to_start

        print("Visited vertex:",current_vertex)
        unvisited_vertices.remove(current_vertex)

    #find and return shortest route
    print(shortest_path_to)
    target_vertex = end
    path = [end]
    while target_vertex != start:
        target_vertex = shortest_path_to[target_vertex]['previous']
        path.insert(0,target_vertex)


    path_tuple = ( shortest_path_to[end]['shortest'], path)
    return path_tuple





#main
if __name__ == "__main__":
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
    print("""(9, [<Vertex: A>, <Vertex: B>, <Vertex: D>, <Vertex: F>])""")
    print(dijkstra_shortest_path(A, F, g))

    print(float('inf'))

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
    print(dijkstra_shortest_path(C, D, g))
    """(7, [ < Vertex: C >, < Vertex: E >, < Vertex: F >, < Vertex: D >])
    (7, [ < Vertex: C >, < Vertex: E >, < Vertex: F >, < Vertex: D >])"""
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
    print(dijkstra_shortest_path(E, D, g))
    """(4, [ < Vertex: E >, < Vertex: F >, < Vertex: D >])"""