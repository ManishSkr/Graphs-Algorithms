"""This is one of the classic example for  Graph Theory and it works using stack"""

def dft(graph,source):
    stack=[]
    stack.append(source)
    result=[]
    while(len(stack)):
        data=stack.pop()
        result.append(data)
        for val in graph[data]:
            stack.append(val)
    return result
    
    # Recursive approach
    # print(source)
    # for neibh in graph[source]:
    #     dft(graph,neibh)
    
        
graph= {'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['F'],
        'E': [],
        'F': []}

print(dft(graph,'A'))