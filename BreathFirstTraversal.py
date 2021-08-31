"""This is also a example of Graph theory as we know it works on queue data stucture"""

def BFT(graph,source):
    queue=[]
    queue.append(source)
    result=[]
    while(len(queue)):
        data=queue.pop(0)
        result.append(data)
        #iterate through all the value of keys and push it to the queue
        for val in graph[data]:
            queue.append(val)
    return result


graph={'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['F'],
        'E': [],
        'F': []}


print(BFT(graph,'A'))