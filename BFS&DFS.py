graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
def BSF(graph,s): #s:start_point
    check_list = [] # checking list
    check_list.append(s)
    seen = set() # seen list
    seen.add(s)
    sq_list = [] # output sequence list
    sq_list.append(s)
    while len(check_list) > 0:
        vertex = check_list.pop(0) # taken out the items
        node = graph[vertex]
        for nodes in node: # check the nodes is seen in graph or not
            if nodes not in seen:#add the nodes that unseen to list
                check_list.append(nodes)
                seen.add(nodes)
                sq_list(nodes)
    return sq_list


def DSF(graph,s): #s:start_point
    stack =[]
    stack.append(s)
    seen = set()
    seen.add(s)
    sq_list = []
    sq_list.append(s)
    while len(stack) > 0 :
        vertex = stack.pop() #choose last one for deep
        node = graph[vertex]
        for nodes in node:
            if nodes not in seen:
                stack.append(nodes)
                seen.add(nodes)
                sq_list.append(nodes)
    return sq_list




# print(BSF(graph, "A"))
print(DSF(graph, "A"))