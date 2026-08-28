def visit(vertex, marked):
    marked[vertex]=True

def neighborhood(vertex, edges, marked, family):
    family.append([vertex])
    neighbor=[]
    for i in edges:
        if i[0]==vertex:
            if not marked[i[1]]:
                neighbor.append(i[1])
                family[-1].append(i[1])
        if i[1]==vertex:
            if not marked[i[0]]:
                neighbor.append(i[0])
                family[-1].append(i[0])
    return neighbor

def bfs(vertices, edges, start, target):
    queue=[]
    family=[]
    marked=[False]*len(vertices)
    result=[]
    if start==target:
        if start not in neighborhood(target, edges, marked, family):
            return start
        else:
            return f"{start} --- {start}"
    visit(start, marked)
    queue.append(start)

    while queue:
        for i in neighborhood(queue[0], edges, marked, family):
            if i==target:
                family[-1].append(i)
                family.reverse()
                j=target
                for i in family:
                    if j in i:
                        result.append(j)
                        j=i[0]
                result.append(j)
                return result
            visit(i, marked)
            queue.append(i)

        queue.pop(0)
    return "No path exists.\n"
