from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file


def bad_arguments(graph, start):
    if graph is None or start is None:
        return True
    if start not in GraphEL.vertices(graph):
        return True


def dfs_helper(graph, start, dfs_future_tup):
    start.set_value("visited")
    dfs_future_tup.append(start)
    
    edges = graph.incident(start)

    for e in edges:
        vertex_1, vertex_2 = e.ends()
        if e._value is None:  # has not been traversed yet
            if vertex_1 == start:
                neighbor = vertex_2
            else:
                neighbor = vertex_1

            if neighbor._value == "visited":
                e.set_value("back")
            else:
                e.set_value("discovery")
                dfs_helper(graph, neighbor, dfs_future_tup)


def dfs(graph, start):
    if (bad_arguments(graph, start)):
        return ()
    dfs_future_tup = []
    dfs_helper(graph, start, dfs_future_tup)
    return tuple(dfs_future_tup)
