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
            counter=0
            for j in i.split():
                if (counter<2):
                    edges.append(j)
                    vertices.add(j)
                else:
                    if j.lower()=="d":
                        edges.append("0")
                    elif j.lower()=="u":
                        edges.append("1")
                counter+=1
    return vertices, edges

def initialize():
    with open(GRAPH, "w") as f:
        print("Enter 'end' to stop.")
        while True:
            edge = input("Enter the edge (e.g. 0 1 d for directed, 0 1 u for undirected): ")
            if edge=="":
                continue
            if edge=="end":
                break
            f.write(edge+'\n')

def check_graph_validity():
    with open(GRAPH, "r") as f:
        for i in f:
            if len(i.split())!=3:
                return -1
            try:
                int(i.split()[0])
                int(i.split()[1])
            except ValueError:
                return -1
            if i.split()[2] not in ("d", "u"):
                return -1