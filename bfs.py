def neighborhood(vertex, edges, marked):
    neighbors=[]
    for i in edges:
        if i[0]==vertex:
            if not marked[i[1]]:
                neighbors.append(i[1])
        if i[1]==vertex:
            if not marked[i[0]]:
                neighbors.append(i[0])
    return neighbors

def bfs(vertices, edges, start, target):
    queue=[]
    parent=[None]*len(vertices)
    marked=[False]*len(vertices)
    result=[]
    if start==target:
        return start
    marked[start]=True
    queue.append(start)

    while queue:
        current=queue[0]
        for i in neighborhood(current, edges, marked):
            parent[i]=current
            marked[i]=True
            if i==target:
                subject=i
                while subject is not None:
                    result.append(subject)
                    subject=parent[subject]
                return result
            queue.append(i)
        queue.pop(0)

    return "No path exists.\n"