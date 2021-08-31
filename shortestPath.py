"""Here we need to return the minimum number of edges between two path i.e shortest path"""

def shortestPath(edges,nodeA,nodeB):
    #we need a helper function to convert edges to a adjacency list
    graph=buildGraph(edges)
    queue=[[nodeA,0]]
    visited=set([nodeA])
    while(len(queue)):
        node,distance=queue.pop(0)
        if(node==nodeB):return distance
        for neighbour in graph[node]:
            #we put the visited check to avoid the cycle as its a undirected graph
            if(neighbour not in visited):
                visited.add(neighbour)
                queue.append([neighbour,distance+1])
    return -1


def buildGraph(edges):
    graph={}
    for edge in edges:
        a,b=edge
        if(a not in graph):graph[a]=[]
        if(b not in graph):graph[b]=[]
        graph[a].append(b)
        graph[b].append(a)
    
    return graph


edges=[
    ['w','x'],
    ['x','y'],
    ['z','y'],
    ['z','v'],
    ['w','v']
]

print(shortestPath(edges,'w','z'))