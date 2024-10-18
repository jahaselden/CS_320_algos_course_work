from edgegraph import VertexEL, EdgeEL, GraphEL, parse_graph_file


def bad_arguments(graph, start):
    if graph is None or start is None:
        return True
    if start not in GraphEL.vertices(graph):
        return True


def dfs_helper(graph, start, visited, dfs_future_tup):
    # VertexEL.set_value(start, "explored")
    dfs_future_tup.append(start)
    # for each edge that is incident to v in graph (for every edge connected to v in G)
    edges = graph.incident(start) # list of edges connected to v
    visited.append(start)
    for e in edges:
        vertex_1, vertex_2 = e.ends()
        # if e is unexplored - meaning: if end vertex of e not in explored_vertices
        if vertex_1 == start:       # then vertex_1 is not a neighbor of starting index
            neighbor = vertex_2     # vertex_2 is neighbor
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

# test
v1 = VertexEL("A")
# you can set a value or weight for v1 using v1.set_value(value)
# you can also use get_value
v2 = VertexEL("B")
v3 = VertexEL("C")
v4 = VertexEL("D")
v5 = VertexEL("E")
v6 = VertexEL("F")
 
# connects v1 and v2 
# set value using e1.set_value(value)
e1 = EdgeEL("e1", v1, v2)
e2 = EdgeEL("e2", v1, v3)
e3 = EdgeEL("e3", v1, v4)
e4 = EdgeEL("e4", v4, v6)
e5 = EdgeEL("e5", v2, v5)
e6 = EdgeEL("e6", v5, v6)
e7 = EdgeEL("e7", v3, v5)
 
# add (add_vertext(v))
# remove (rm_vertex())
# add edges using add_edge(e) - if vertices in edge are not in graph they get added
graph = GraphEL()
graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex(v4)
graph.add_vertex(v5)
graph.add_vertex(v6)
 
graph.add_edge(e1)
graph.add_edge(e2)
graph.add_edge(e3)
graph.add_edge(e4)
graph.add_edge(e5)
graph.add_edge(e6)
 
dfs_order = dfs(graph, v1)
print(dfs_order)