"""Here we use bft or dft to check wheather we were able to traverse from source to destination or not."""

def haspath(graph,source,destination):
    # #we use depth first traversal here
    # if(source==destination):
    #     return True
    # # I use recursion here rather than stack
    # for neighbour in graph[source]:
    #    if(haspath(graph,neighbour,destination)==True):
    #        return True
 
    # return False
    #we use breath first traversal here
    queue=[]
    queue.append(source)
    while(len(queue)):
        data=queue.pop(0)
        if(data==destination):
                return True
        for neighbour in graph[data]:
            queue.append(neighbour)
           
    
    return False
graph={'f':['g','i'],
        'g':['h'],
        'h':[],
        'i':['g','k'],
        'j':['í'],
        'k':[]}

print(haspath(graph,'f','k'))