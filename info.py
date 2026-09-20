from pathlib import Path
import os

GRAPH=Path(__file__).parent/"graph.txt"
BFS=Path(__file__).parent/"bfs.exe" if os.name=="nt" else Path(__file__).parent/"bfs"
DFS=Path(__file__).parent/"dfs.exe" if os.name=="nt" else Path(__file__).parent/"dfs"
EXE_BFS="bfs.exe" if os.name=="nt" else "./bfs"
EXE_DFS="dfs.exe" if os.name=="nt" else "./dfs"

def information():
    vertices=set()
    edges=[]
    with open(GRAPH, "r") as f:
        for i in f:
            for j in i.split():
                edges.append(j)
                vertices.add(j)
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
