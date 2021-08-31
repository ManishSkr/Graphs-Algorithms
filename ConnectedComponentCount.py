"""This is also one of the variation of graph, here we given a adjacency list and we need to return the count
of connected componenets present in the graph"""


def connected(graph):
    visited=set()
    count=0
    for key in graph.keys():
        #we explore all the coonnected component of the given key
        if(explore(graph,key,visited)):
            count+=1
    return count

def explore(graph,key,visited):
    #we follow the dfs using recursive approach for the traversal
    if(key in visited):return False
    visited.add(key)
    for neighbour in graph[key]:
        explore(graph,neighbour,visited)
    return True

graph={
    0:[0,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]

}
print(connected(graph))