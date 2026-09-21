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
    while True:
        check = info.check_graph_validity()
        if check==-1:
            decision=ui.broken_graph()
            if decision=="":
                choice= ui.ask_graph_reset()
                if choice=="y":
                    ui.clear()
                    info.initialize()
                    ui.clear()
            else: exit(0)
        else: break
        
    vertices, edges = info.information()
    if not info.BFS.exists():
        subprocess.run(
            ["g++", "bfs.cpp", "-o", info.BFS]
        )
    if not info.DFS.exists():
        subprocess.run(
            ["g++", "dfs.cpp", "-o", info.DFS]
        )
    while True:
            menu_choice = ui.get_algorithms_menu()
            if menu_choice=='1':
            
                start, target = ui.get_vertices_bfs()
                try:
                    result = subprocess.run(
                        [info.EXE_BFS, " ".join(vertices), " ".join(edges), start, target],
                        capture_output=True,
                        text=True
                    )
                    result= result.stdout.split()
                    print(ui.display_bfs(result))
                except IndexError:
                    print("The root vertex does not exist.")
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue
            elif menu_choice=='2':

                root= ui.get_root_dfs()
                try:
                    result = subprocess.run(
                        [info.EXE_DFS, " ".join(vertices), " ".join(edges), root],
                        capture_output=True,
                        text=True
                    )
                    result= result.stdout.split()
                    print(ui.display_dfs(result))
                except IndexError:
                    print("Vertex does not exist.")
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue

            else:
                break

if __name__=="__main__":
    main()