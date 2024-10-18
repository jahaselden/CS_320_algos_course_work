from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file


def bad_arguments(graph, start):
    if graph is None or start is None:
        return True
    if start not in GraphEL.vertices(graph):
        return True


def dfs_helper(graph, start, visited, dfs_future_tup):
    visited.append(start)
    dfs_future_tup.append(start)
    
    edges = graph.incident(start)

    for e in edges:
        vertex_1, vertex_2 = e.ends()

        if vertex_1 == start:
            neighbor = vertex_2
        else:
            neighbor = vertex_1
        
        if neighbor in visited:
            e.set_value("back")
        else:
            e.set_value("discovery")
            dfs_helper(graph, neighbor, visited, dfs_future_tup)


def dfs(graph, start):
    if (bad_arguments(graph, start)):
        return ()
    
    visited = []
    dfs_future_tup = []
    dfs_helper(graph, start, visited, dfs_future_tup)
    return tuple(dfs_future_tup)
