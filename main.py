import subprocess
import ui, info

def main():
    if not info.GRAPH.exists():
        ui.clear()
        info.initialize()
        ui.clear()
    else:
        choice = ui.ask_graph_reset()
        if choice=='y':
            ui.clear()
            info.initialize()
            ui.clear()
    vertices, edges = info.information()
    if not info.BFS.exists():
        subprocess.run(
            ["g++", "bfs.cpp", "-o", "bfs"]
        )
    if not info.DFS.exists():
        subprocess.run(
            ["g++", "dfs.cpp", "-o", "dfs"]
        )
    while True:
            algorithm = ui.get_algorithms()
            if algorithm=='1':
            
                start, target = ui.get_vertices_bfs()
                try:
                    result = subprocess.run(
                        ["./bfs", " ".join(vertices), " ".join(edges), start, target],
                        capture_output=True,
                        text=True
                    )
                    result= result.stdout.split()
                    print(ui.display(result))
                except IndexError:
                    print("The root vertex does not exist.")
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue
            else:

                root= ui.get_root_dfs()
                try:
                    result = subprocess.run(
                        ["./dfs", " ".join(vertices), " ".join(edges), root],
                        capture_output=True,
                        text=True
                    )
                    result= result.stdout.split()
                    print(ui.display(result))
                except IndexError:
                    print("Vertex does not exist.")
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue

if __name__=="__main__":
    main()