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
    while True:
            algorithm = ui.get_algorithms()
            if algorithm=='1':
            
                start, target = ui.get_vertices_bfs()
                result = subprocess.run(
                    ["./bfs", " ".join(vertices), " ".join(edges), "".join(start), "".join(target)],
                    capture_output=True,
                    text=True
                )
                result= result.stdout.split()
                print(ui.display(result))
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue
            else:

                root= ui.get_root_dfs()
                result = subprocess.run(
                    ["./dfs", " ".join(vertices), " ".join(edges), "".join(root)],
                    capture_output=True,
                    text=True
                )
                result= result.stdout.split()
                print(ui.display(result))
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue

if __name__=="__main__":
    main()