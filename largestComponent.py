"""here we need to return the largest component which have maximum number of nodes, This is also one of the
classic example of graph."""

def largestComponent(graph):
    visited=set()
    count=0
    maxCount=0
    for key in graph.keys():
        count=explore(graph,key,visited)
        if(count>maxCount):
            maxCount=count
        
    return maxCount

def explore(graph,val,visited):
    #Here instead of false we pass 0 if node is in visited
    if(val in visited):return 0

    visited.add(val)
    count=1
    for neighbour in graph[val]:
        count+=explore(graph,neighbour,visited)
    
    return count

graph={
    0:[8,1,5],
    1:[0],
    5:[0,8],
    8:[0,5],
    2:[3,4],
    3:[2,4],
    4:[3,2]
}

print(largestComponent(graph))