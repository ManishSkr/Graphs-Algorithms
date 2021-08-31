"""here we write a function, undirected path, that takes in an array of edges for an undirected graph and two
nodes (nodeA, nodeB). The function sould return a boolean indicating whether or not there exists a path between
nodeA and nodeB"""

def undirectedPath(edges,source,destination):
    # we call a  helper function to return edges to adjacency list
    graph=buildGraph(edges)
    return hasPath(graph,source, destination,set())

def buildGraph(edges):
    graph={}
    for edge in edges:
        a,b=edge
        if(a not in graph):graph[a]=[]
        if(b not in graph):graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def hasPath(graph,source,destination,visited):
    if(source==destination):
        return True
    # write condition to avoid cycles in the graph
    if(source in visited):return False
    visited.add(source)

    for neighbour in graph[source]:
        if(hasPath(graph,neighbour,destination,visited)==True):
            return True
    return False

edges=[
    ['i','j'],
    ['k','i'],
    ['n','k'],
    ['k','l'],
    ['o','n'],

]
print(undirectedPath(edges,'i','o'))