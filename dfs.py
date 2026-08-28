def visit(vertex, marked):
    marked[vertex]=True

def neighborhood(vertex, edges):
    neighbors=[]
    for i in edges:
        if i[0]==vertex:
            if not i[1] in neighbors:
                neighbors.append(i[1])
        if i[1]==vertex:
            if not i[0] in neighbors:
                neighbors.append(i[0])
    return neighbors

def dfs(vertices, edges, root):
    marked=[False]*len(vertices)
    result=[]
    def explore(vertex):
        visit(vertex, marked)
        result.append(vertex)
        for i in neighborhood(vertex, edges):
            if i==vertex:
                result.append(i)
            if not marked[i]:
                explore(i)
    explore(root)
    result.pop(0)
    if result:
        return result
    else:
        return "The root vertex is isolated; no other vertices are reachable from it.\n"