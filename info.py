from pathlib import Path

GRAPH=Path(__file__).parent/"graph.txt"

def information():
    vertices=set()
    edges=[]
    with open(GRAPH, "r") as f:
        for i in f:
            edges.append([])
            for j in i.split():
                edges[-1].append(int(j))
                vertices.add(int(j))
    return vertices, edges

def initialize():
    with open(GRAPH, "w") as f:
        print("Enter 'end' to stop.")
        while True:
            edge = input("Enter the edge (e.g. 0 1): ")
            if edge=="":
                continue
            if edge=="end":
                break
            f.write(edge+'\n')
