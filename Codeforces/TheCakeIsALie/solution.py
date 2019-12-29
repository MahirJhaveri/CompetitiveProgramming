# 1282E - The Cake Is A Lie


def get_edge(vertex1, vertex2):
    return (vertex1, vertex2) if vertex1 < vertex2 else (vertex2, vertex1)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        n = int(input())
        pieces = []
        for c in range(n-2):
            inp = input().rstrip().split(" ")
            pieces.append([int(inp[0]), int(inp[1]), int(inp[2])])

        # Preparing the graph
        G = {}
        piece_index = 0
        while piece_index < len(pieces):
            for vertex in pieces[piece_index]:
                if vertex not in G:
                    G[vertex] = {}
                G[vertex][piece_index] = True
            piece_index += 1

        # prepare list of vertices associated with only one piece
        # That piece can be safely removed
        next_vertices = []
        for vertex in G:
            if len(G[vertex]) == 1:
                next_vertices.append(vertex)

        q = []
        border_edges = {}
        non_border_edges = {}
        while len(next_vertices) > 0:
            v = next_vertices.pop()
            if len(G[v]) > 0:
                piece_index = list(G[v].keys()).pop()
                q.append(str(piece_index+1))
                piece = pieces[piece_index]
                G.pop(v)
                for vertex_index in range(3):
                    vertex = piece[vertex_index]
                    if vertex != v:
                        G[vertex].pop(piece_index)
                        if len(G[vertex]) == 1:
                            next_vertices.append(vertex)
                        edge = get_edge(v, vertex)
                        if edge not in non_border_edges:
                            border_edges[edge] = True
                    else:
                        swap(piece, 0, vertex_index)
                edge = get_edge(piece[1], piece[2])
                non_border_edges[edge] = True

        border_edges = list(border_edges.keys())
        vertices = {}
        for a, b in border_edges:
            if a not in vertices:
                vertices[a] = {}
            if b not in vertices:
                vertices[b] = {}
            vertices[a][b] = True
            vertices[b][a] = True

        start = None
        start_val = 5000000000
        for vertex in vertices:
            if len(vertices[vertex]) < start_val:
                start = vertex
                start_val = len(vertices[vertex])

        v = start
        p = []
        while len(p) < n:
            p.append(str(v))
            assert len(vertices[v]) <= 1
            if len(vertices[v]) == 1:
                neighbor = list(vertices[v].keys()).pop()
                vertices[neighbor].pop(v)
                v = neighbor

        print(" ".join(p))
        print(" ".join(q))
